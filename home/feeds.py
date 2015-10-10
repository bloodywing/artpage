from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.text import  SafeText
from django.utils.feedgenerator import Atom1Feed
from home.models import ImagePage

import re

__author__ = 'pierre'


class ImgdumpRSSFeed(Feed):


    title = 'Imagedump and WIP RSS Feed'
    description = 'My WIP and image dumps, some of them might never be finished'

    def item_link(self, item):
        return item.value.get_rendition('original').url

    def get_object(self, request, *args, **kwargs):
        self.obj = ImagePage.objects.live().get(pk=request.GET['id'])
        self.link = self.obj.full_url
        return None

    def items(self):
        return self.obj.body

    def item_title(self, item):
        return self.obj.title

    def item_description(self, item):
        return item.render()


class ImgdumpAtomFeed(ImgdumpRSSFeed):

    title = 'Imagedump and WIP Atom Feed'
    feed_type = Atom1Feed
    subtitle = ImgdumpRSSFeed.description
