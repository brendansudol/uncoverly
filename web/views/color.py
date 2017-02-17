from django.shortcuts import redirect
from django.views.generic import ListView

from web.models import Product


class ColorView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 48
    template_name = 'web/color.html'

    def dispatch(self, *args, **kwargs):
        self.hex = self.kwargs['hex']

        if len(self.hex) != 6:
            return redirect('web:home')

        return super(ColorView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        dist = int(self.request.GET.get('d', 50))

        qs = self.model.objects \
            .color_search(self.hex, dist) \
            .filter(is_visible=True) \
            .order_by('rand2')

        return qs

    def get_context_data(self, **kwargs):
        context = super(ColorView, self).get_context_data(**kwargs)

        context.update({
            'hex': self.hex,
            'total': self.get_queryset().count(),
        })

        return context
