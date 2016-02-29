from django.conf.urls import patterns, url

from web.views.favorite import FavoriteView, FavoritesView
from web.views.logout import LogoutView
from web.views.misc import (
    AboutView, ContactView, PrivacyView, TermsView
)
from web.views.product import ProductView
from web.views.home import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
    url(r'^terms$', TermsView.as_view(), name='terms'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProductView.as_view(), name='product'),
    url(r'^favorite/(?P<pid>[\w/\-]+)?$', FavoriteView.as_view(), name='fave'),
    url(r'^favorites$', FavoritesView.as_view(), name='faves'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
