from django.conf.urls import patterns, url
# from django.views.decorators.cache import cache_page

from web.views.auth import LoginView, LogoutView, SignupView
from web.views.category import CategoriesView, CategoryView
from web.views.favorite import FavoriteView, FavoritesView
from web.views.find import FindView, FindsView
from web.views.home import HomeView
from web.views.misc import (
    AboutView, ContactView, PrivacyView, TermsView
)
from web.views.newsletter import NewsletterView
from web.views.product import ProductView
from web.views.seller import SellerView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
    url(r'^terms$', TermsView.as_view(), name='terms'),
    url(r'^newsletter$', NewsletterView.as_view(), name='newsletter'),
    url(
        r'^categories$',
        # cache_page(60 * 5)(CategoriesView.as_view()),
        CategoriesView.as_view(),
        name='categories'
    ),
    url(r'^c/(?P<cat>[\w/\-]+)?$', CategoryView.as_view(), name='category'),
    url(r'^s/(?P<pk>[\w/\-]+)?$', SellerView.as_view(), name='seller'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProductView.as_view(), name='product'),
    url(r'^favorite/(?P<pid>[\w/\-]+)?$', FavoriteView.as_view(), name='fave'),
    url(
        r'^u/(?P<uid>[\w/\-]+)/favorites$',
        FavoritesView.as_view(),
        name='faves'
    ),
    url(r'^find$', FindView.as_view(), name='find'),
    url(
        r'^u/(?P<uid>[\w/\-]+)/finds$',
        FindsView.as_view(),
        name='finds'
    ),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^join$', SignupView.as_view(), name='signup'),
)
