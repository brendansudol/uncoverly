from django.views.generic.detail import DetailView

from web.models import Product


class ProductView(DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'web/product.html'
