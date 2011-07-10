from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('localqrgen.api.views',
    url(r'^check/$', 'check_qrcode', name='check-qrcode'),
    url(r'^stats/$', 'stats', name='stats'),
)
