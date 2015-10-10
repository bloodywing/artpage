from __future__ import unicode_literals

from django.db import models
from django.db.models import ImageField, TextField
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import *
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.fields import *

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet
from blog.models import RelatedLink


@register_snippet
class SocialLabel(models.Model):
    url = models.URLField(null=True, blank=False)
    color = models.CharField(max_length=6, help_text='Color in HTML Color Code, HEX: #xxxxxx')
    text = models.CharField(null=True, blank=True, max_length=255)
    icon = models.CharField(null=True, blank=True, max_length=50, help_text='Fontawesome Iconname eg: facebook, twitter, instagram')

    panels = [
        FieldPanel('url'),
        FieldPanel('color'),
        FieldPanel('text'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.text


class JumbotronBlock(blocks.StructBlock):

    headline = blocks.CharBlock()
    lead = blocks.RichTextBlock(classname='full')


class ImagePage(Page):

    body = StreamField([
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class Simplepage(Page):

    body = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]


class HomePage(Page):

    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock(classname='full')),
        ('image', ImageChooserBlock()),
        ('html', RawHTMLBlock()),
        ('embed', EmbedBlock()),
        ('jumbotron', JumbotronBlock())
    ])

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        InlinePanel('related_links', label="Related links"),
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


class LinkwithImage(LinkFields):

    title = models.CharField(max_length=255, help_text='Link title')
    image = models.ForeignKey(
        'gallery.ExtendedImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    text = models.TextField(blank=True)

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('text', classname='full'),
        MultiFieldPanel(LinkFields.panels, 'Link')
    ]

    class Meta:
        abstract = True

class PageRelatedLink(Orderable, LinkwithImage):
    page = ParentalKey('HomePage', related_name='related_links')
