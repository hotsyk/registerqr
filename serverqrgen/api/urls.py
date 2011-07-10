from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^v1/', include('serverqrgen.api.urls_v1')),
)
