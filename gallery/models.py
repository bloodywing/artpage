from django.db import models

# Create your models here.
from django.db.models import TextField
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailadmin.taggable import TagSearchable
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.models import Image, AbstractImage, AbstractRendition
from wagtail.wagtailsearch import index
import os


class ExtendedImage(AbstractImage, TagSearchable):

    description = TextField(blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'description',
    )

    search_fields = TagSearchable.search_fields + (
        index.SearchField('description', partial_match=True, boost=10),
        #index.SearchField('get_tags', partial_match=True, boost=10),
    )

    @property
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension


class ExtendedRendition(AbstractRendition):

    image = models.ForeignKey(ExtendedImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )

# Delete the source image file when an image is deleted
@receiver(pre_delete, sender=ExtendedImage)
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)


# Delete the rendition image file when a rendition is deleted
@receiver(pre_delete, sender=ExtendedRendition)
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)


class GalleryImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    image.description = blocks.RichTextBlock()


class GalleryPage(Page, index.Indexed):

    body = StreamField(
        [
            ('picturelist', blocks.ListBlock(
                GalleryImageBlock()
            )),
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]