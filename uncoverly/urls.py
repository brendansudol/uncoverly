from django.conf.urls import include, url
from django.contrib import admin

handler404 = 'web.views.errors.handler404'
handler500 = 'web.views.errors.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^auth/', include('social_django.urls', namespace='social')),
    url(r'^', include('web.urls', namespace='web')),
]
