from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap
from django.views.generic import TemplateView

from blog.feeds import BlogPostRSSFeed, BlogPostAtomFeed
from home.feeds import ImgdumpRSSFeed, ImgdumpAtomFeed

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, name='sitemap'),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', 'search.views.search', name='search'),
    url(r'', include(wagtail_urls)),
    url(r'^latest/feed/rss$', BlogPostRSSFeed()),
    url(r'^latest/feed/atom$', BlogPostAtomFeed()),

    url(r'^rss_bloodys_blog$', BlogPostRSSFeed()),
    url(r'^atom_bloodys_blog$', BlogPostAtomFeed()),

    url(r'^latest/feed/imgdump_rss$', ImgdumpRSSFeed()),
    url(r'^latest/feed/imgdump_atom$', ImgdumpAtomFeed())
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
