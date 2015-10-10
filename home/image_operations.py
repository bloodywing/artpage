from wagtail.wagtailimages.image_operations import Operation

from PIL import ImageFilter, ImageEnhance
from wagtail.wagtailimages.models import Filter
from willow.backends.pillow import PillowBackend

__author__ = 'pierre'

@PillowBackend.register_operation('blur')
def blur(backend, blur):
    im = backend.image.filter(ImageFilter.GaussianBlur(int(blur)))
    backend.image = im


@PillowBackend.register_operation('sharpen')
def sharpen(backend, sharpness):
    s = ImageEnhance.Sharpness(backend.image)
    backend.image = s.enhance(sharpness).copy()

@PillowBackend.register_operation('contrast')
def sharpen(backend, contrast):
    s = ImageEnhance.Contrast(backend.image)
    backend.image = s.enhance(contrast).copy()


@PillowBackend.register_operation('detail')
def detail(backend):
    im = backend.image.filter(ImageFilter.DETAIL)
    backend.image = im

class ContrastOperation(Operation):

    vary_fields = ('focal_point_width', 'focal_point_height', 'focal_point_x', 'focal_point_y')

    def construct(self, contrast, *args):
        self.contrast = contrast
        self.extrafilter = None
        if len(args):
            self.extrafilter = Filter._registered_operations[args[0]](*args)

    def run(self, willow, image):
        willow.contrast(float(self.contrast))
        print(image.get_focal_point())

        self.extrafilter.run(willow, image)

class SharpenOperation(Operation):

    vary_fields = ('focal_point_width', 'focal_point_height', 'focal_point_x', 'focal_point_y')

    def construct(self, sharpness, *args):
        self.sharpness = sharpness
        self.extrafilter = None
        if len(args):
            self.extrafilter = Filter._registered_operations[args[0]](*args)

    def run(self, willow, image):
        self.extrafilter.run(willow, image)
        willow.sharpen(float(self.sharpness))


class DetailOperation(Operation):

    vary_fields = ('focal_point_width', 'focal_point_height', 'focal_point_x', 'focal_point_y')

    def construct(self, *args):
        self.extrafilter = None
        if len(args):
            self.extrafilter = Filter._registered_operations[args[0]](*args)

    def run(self, willow, image):
        self.extrafilter.run(willow, image)
        willow.detail()

class BlurOperation(Operation):

    vary_fields = ('focal_point_width', 'focal_point_height', 'focal_point_x', 'focal_point_y')

    def construct(self, blur, *args):
        self.blur = blur
        self.extrafilter = None
        if len(args):
            self.extrafilter = Filter._registered_operations[args[0]](*args)

    def run(self, willow, image):
        self.extrafilter.run(willow, image)
        willow.blur(self.blur)
