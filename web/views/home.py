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

        return qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['favorites'] = self.get_user_faves()
        return context

    def get_user_faves(self):
        if not self.request.user.is_authenticated():
            return []

        favorites = self.request.user.favorites \
            .filter(product_id__in=(i.pk for i in self.get_queryset())) \
            .values_list('product_id', flat=True)

        return favorites
