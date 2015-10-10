from wagtail.wagtailimages.models import AbstractImage, Image

__author__ = 'pierre'


class ExtendedImage(AbstractImage):

    admin_form_fields = Image.admin_form_fields + (
        'description',
    )