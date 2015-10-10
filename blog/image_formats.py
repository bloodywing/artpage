__author__ = 'pierre'

from wagtail.wagtailimages.formats import Format, register_image_format

register_image_format(Format('thumbnail', 'Thumbnail', 'richtext-image thumbnail', 'max-120x120'))
register_image_format(Format('400pxawww', '400px width', 'richtext-image 400pxawww', 'width-400'))
register_image_format(Format('original', 'Original', 'richtext-image original', 'original'))