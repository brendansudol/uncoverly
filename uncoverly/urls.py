from django.conf.urls import patterns, include, url
from django.contrib import admin


handler404 = 'web.views.errors.handler404'
handler500 = 'web.views.errors.handler500'


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('^auth/', include('social_django.urls', namespace='social')),
    url(r'^', include('web.urls', namespace='web')),
)
