from datetime import datetime

from django.views.generic import TemplateView

from web.models import Seller


class FeaturedSellerView(TemplateView):
    template_name = 'web/featured.html'

    def get_context_data(self, **kwargs):
        context = super(FeaturedSellerView, self).get_context_data(**kwargs)

        sellers = Seller.objects \
            .order_by('created') \
            .all()[:4]

        context.update({
            'today': datetime.today().date(),
            'sellers': sellers,
        })

        return context
