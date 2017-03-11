from django.views.generic.detail import DetailView

from web.models import Product
from web.util.categories import CAT_ID_LOOKUP


class ProductView(DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'web/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)

        context.update({
            'more_category': self.more_by_category(),
            'more_seller': self.more_by_seller(),
            'cat_id': CAT_ID_LOOKUP.get(self.object.category),
        })

        return context

    def more_by_category(self):
        category = self.object.category

        if not category:
            return []

        return Product.objects \
            .filter(is_visible=True) \
            .filter(taxonomy__0=category) \
            .exclude(pk=self.object.pk) \
            .all()[:6]

    def more_by_seller(self):
        seller = self.object.seller

        if not seller:
            return []

        return Product.objects \
            .filter(is_visible=True) \
            .filter(seller=seller) \
            .exclude(pk=self.object.pk) \
            .all()[:4]
