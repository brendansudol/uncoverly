from django.conf.urls import patterns, url

from web.views.category import CategoryView
from web.views.favorite import FavoriteView, FavoritesView
from web.views.find import FindsView
from web.views.home import HomeView
from web.views.logout import LogoutView
from web.views.misc import (
    AboutView, ContactView, PrivacyView, TermsView
)
from web.views.product import ProductView
from web.views.seller import SellerView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
    url(r'^terms$', TermsView.as_view(), name='terms'),
    url(r'^c/(?P<cat>[\w/\-]+)?$', CategoryView.as_view(), name='category'),
    url(r'^s/(?P<pk>[\w/\-]+)?$', SellerView.as_view(), name='seller'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProductView.as_view(), name='product'),
    url(r'^favorite/(?P<pid>[\w/\-]+)?$', FavoriteView.as_view(), name='fave'),
    url(r'^favorites$', FavoritesView.as_view(), name='faves'),
    url(r'^finds$', FindsView.as_view(), name='finds'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
