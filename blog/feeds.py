from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.text import  SafeText
from django.utils.feedgenerator import Atom1Feed
from blog.models import BlogPage

import re

__author__ = 'pierre'


class BlogPostRSSFeed(Feed):


    title = getattr(settings, 'WAGTAIL_BLOG_FEED_TITLE', 'RSS Feed')
    description = getattr(settings, 'WAGTAIL_BLOG_FEED_DESCRIPTION', 'Blog Post Feed')

    link = '/blog/'

    def items(self):
        return BlogPage.objects.live().order_by('-date')[:getattr(settings, 'WAGTAIL_BLOG_FEED_LENGTH', 50)]

    def item_title(self, item):
        return item.title

    def item_description(self, item):

        #desc = re.compile(r'<.*?>').sub('', item.intro)
        desc = item.intro
        return desc


class BlogPostAtomFeed(BlogPostRSSFeed):

    title = getattr(settings, 'WAGTAIL_BLOG_FEED_TITLE', 'Atom Feed')
    feed_type = Atom1Feed
    subtitle = BlogPostRSSFeed.description
