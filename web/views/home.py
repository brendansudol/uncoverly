from django.views.generic import ListView

from web.models import Product


class HomeView(ListView):
    context_object_name = 'products'
    model = Product
    ordering = '-created'
    paginate_by = 12
    template_name = 'web/home.html'

    def get_queryset(self):
        qs = super(HomeView, self).get_queryset()
        get = self.request.GET

        q = get.get('q')
        if q is not None:
            qs = self.model.objects.search(q)

        p = get.get('price')
        if p is not None:
            try:
                qs = qs.filter(price_usd__lte=(int(p) * 100))
            except Exception:
                pass

        return qs.filter(is_visible=True).order_by('rand1')
