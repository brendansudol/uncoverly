from django.conf.urls import patterns, url

from web.views.about import AboutView
from web.views.logout import LogoutView
from web.views.home import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
