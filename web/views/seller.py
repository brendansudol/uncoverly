from django.views.generic.detail import DetailView

from web.models import Product, Seller


class SellerView(DetailView):
    context_object_name = 'seller'
    model = Seller
    template_name = 'web/seller.html'

    def get_context_data(self, **kwargs):
        context = super(SellerView, self).get_context_data(**kwargs)

        context['products'] = Product.objects \
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
