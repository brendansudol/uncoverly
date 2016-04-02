from django.views.generic.detail import DetailView

from web.models import Product


class ProductView(DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'web/product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)

        context.update({
            'more_category': self.more_by_category(),
            'more_seller': self.more_by_seller(),
        })

        return context

    def more_by_category(self):
        category = self.object.category

        if not category:
            return []

        return Product.objects \
            .filter(category=category) \
            .exclude(pk=self.object.pk) \
            .all()[:8]

    def more_by_seller(self):
        seller = self.object.seller

        if not seller:
            return []

        return Product.objects \
            .filter(seller=seller) \
            .exclude(pk=self.object.pk) \
            .all()[:4]
