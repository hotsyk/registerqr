from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^submit/', 'serverqrgen.api.views.submit_job'),
    #url(r'^update/', 'serverqrgen.api.views.update_job'),
    #url(r'^getqr/', 'serverqrgen.api.views.get_qr'),
)
