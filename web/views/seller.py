from django.views.generic import ListView
from django.views.generic.detail import DetailView

from web.models import Product, Seller


class SellersView(ListView):
    context_object_name = 'sellers'
    model = Seller
    ordering = '-created'
    paginate_by = 4
    template_name = 'web/sellers.html'

    def get_queryset(self):
        qs = super(SellersView, self).get_queryset()
        return qs.filter(visible_product_count__gte=4)


class SellerView(DetailView):
    context_object_name = 'seller'
    model = Seller
    template_name = 'web/seller.html'

    def get_context_data(self, **kwargs):
        context = super(SellerView, self).get_context_data(**kwargs)

        context['products'] = Product.objects \
            .filter(is_visible=True) \
            .filter(seller__pk=self.kwargs['pk']) \
            .order_by('-created')

        context['site'] = self.get_site_info()

        return context

    def get_site_info(self):
        site = (self.object.social or {}).get('shop-website')

        if not site:
            return

        return {
            'full_url': site,
            'display': ''.join(site.split('www.')[1:]) or site,
        }
