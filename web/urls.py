from django.conf.urls import url

from web.views.about import AboutView
from web.views.auth import LoginView, LogoutView, SignupView
from web.views.category import CategoriesView, CategoryView
from web.views.color import ColorView
from web.views.favorite import FavoriteView, FavoritesView
from web.views.find import FindView, FindsView
from web.views.home import HomeView
from web.views.misc import ContactView, PrivacyView, QuizView, TermsView
from web.views.newsletter import NewsletterView
from web.views.product import ProductView
from web.views.search import SearchView
from web.views.seller import SellerView, SellersView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^c/(?P<cat>[\w/\-]+)?$', CategoryView.as_view(), name='category'),
    url(r'^categories$', CategoriesView.as_view(), name='categories'),
    url(r'^color/(?P<hex>[\w/\-]+)?$', ColorView.as_view(), name='color'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^favorite/(?P<pid>[\w/\-]+)?$', FavoriteView.as_view(), name='fave'),
    url(r'^find$', FindView.as_view(), name='find'),
    url(r'^join$', SignupView.as_view(), name='signup'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^newsletter$', NewsletterView.as_view(), name='newsletter'),
    url(r'^p/(?P<pk>[\w/\-]+)?$', ProductView.as_view(), name='product'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
    url(r'^quiz$', QuizView.as_view(), name='quiz'),
    url(r'^s/(?P<pk>[\w/\-]+)?$', SellerView.as_view(), name='seller'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^shops$', SellersView.as_view(), name='shops'),
    url(r'^terms$', TermsView.as_view(), name='terms'),
    url(
        r'^u/(?P<uid>[\w/\-]+)/favorites$',
        FavoritesView.as_view(),
        name='faves'
    ),
    url(
        r'^u/(?P<uid>[\w/\-]+)/finds$',
        FindsView.as_view(),
        name='finds'
    ),
]
