from django import template
from blog.models import *

register = template.Library()

__author__ = 'pierre'

@register.inclusion_tag('blog/tags/social_widgets.html', takes_context=True)
def social_widgets(context):
    print(SocialWidget.objects.all())
    return {
        'social_widgets': SocialWidget.objects.all(),
        'request': context['request']
    }
