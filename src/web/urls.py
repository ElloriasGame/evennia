#
# File that determines what each URL points to. This uses _Python_ regular
# expressions, not Perl's.
#
# See:
# http://diveintopython.org/regular_expressions/street_addresses.html#re.matching.2.3
#

from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

# fix to resolve lazy-loading bug
# https://code.djangoproject.com/ticket/10405#comment:11
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()

# loop over all settings.INSTALLED_APPS and execute code in
# files named admin.py in each such app (this will add those
# models to the admin site)
admin.autodiscover()

# Setup the root url tree from /

urlpatterns = [
    # User Authentication
    url(r'^accounts/login',  'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout', name="logout"),

    # News stuff
    # url(r'^news/', include('src.web.news.urls')),

    # Page place-holder for things that aren't implemented yet.
    url(r'^tbi/', 'src.web.views.to_be_implemented', name='to_be_implemented'),

    # Admin interface
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # favicon
    url(r'^favicon\.ico$',  RedirectView.as_view(url='/media/images/favicon.ico')),

    # ajax stuff
    url(r'^webclient/', include('src.web.webclient.urls', namespace='webclient', app_name='webclient')),

    # Front page
    url(r'^$', 'src.web.views.page_index', name="index")]

# This sets up the server if the user want to run the Django
# test server (this should normally not be needed).
if settings.SERVE_MEDIA:
    urlpatterns.extend([
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
    ])
