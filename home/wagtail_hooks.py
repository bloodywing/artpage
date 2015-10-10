from wagtail.wagtailcore import hooks
from home import image_operations

__author__ = 'pierre'


@hooks.register('register_image_operations')
def register_image_operations():
    return [
        ('blur', image_operations.BlurOperation),
        ('detail', image_operations.DetailOperation),
        ('sharpen', image_operations.SharpenOperation),
        ('contrast', image_operations.ContrastOperation),
    ]