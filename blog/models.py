from django.core.paginator import Paginator, PageNotAnInteger
from django.db import models

# Create your models here.
from django.db.models import TextField
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel, InlinePanel, \
    StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index
from gallery.models import ExtendedImage

@register_snippet
class SocialWidget(models.Model):
    html = TextField(blank=True)

    panels = [
        FieldPanel('html',  classname="full"),
    ]

    def __str__(self):
        return self.html


class BlogPage(Page):


    main_image = models.ForeignKey(
        ExtendedImage,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateField('Post Date')
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('embed', EmbedBlock()),
    ])

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    def get_absolute_url(self):
        return self.full_url
    
    @property
    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('related_links', label='Related Links')
    ]


class LinkFields(models.Model):
    link_external = models.URLField('External Link', blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):

    title = models.CharField(max_length=255, help_text='Link title')

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, 'Link')
    ]

    class Meta:
        abstract = True


class BlogPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('blog.BlogPage', related_name='related_links')


class BlogIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('blog.BlogIndexPage', related_name='related_links')


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def blogs(self):
        """
        All blog post pages
        :return:
        """

        blogs = BlogPage.objects.live().descendant_of(self)

        # Order by Date, recent first

        blogs = blogs.order_by('-date')

        return blogs


    def get_context(self, request, *args, **kwargs):

        blogs = self.blogs

        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs

        return context


    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('related_links', label='Related Links')
    ]