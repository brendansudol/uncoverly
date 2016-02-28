from django.conf.urls import patterns, url

from web.views.about import AboutView
from web.views.favorite import FavoriteView, FavoritesView
from web.views.logout import LogoutView
from web.views.home import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^favorite/(?P<pid>[\w/\-]+)?$', FavoriteView.as_view(), name='fave'),
    url(r'^favorites$', FavoritesView.as_view(), name='faves'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
