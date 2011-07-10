from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverqrgen.views.home', name='home'),
    # url(r'^serverqrgen/', include('serverqrgen.foo.urls')),
    url(r'api/', include('serverqrgen.api.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
