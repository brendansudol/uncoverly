from django.http import Http404
from django.views.generic import ListView

from web.models import Product


class CategoryView(ListView):
    context_object_name = 'products'
    model = Product
    ordering = '-created'
    paginate_by = 12
    template_name = 'web/home.html'

    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()

        category = self.kwargs['cat']
        if category not in ['abc', 'def']:
            raise Http404("Bad category")

        return qs.filter(category=category)
