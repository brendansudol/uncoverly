from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from web.models import Product
from web.util.categories import CATEGORIES, CAT_NAME_LOOKUP


class CategoriesView(TemplateView):
    template_name = 'web/categories.html'
    product_limit = 6

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)

        context.update({
            'now': datetime.now(),
            'categories': self.products_by_category(),
        })

        return context

    def products_by_category(self):
        data = []

        for c in CATEGORIES:
            data.append({
                'id': c['id'],
                'display': c['name'],
                'products': self.product_sample(c['name']),
            })

        return data

    def product_sample(self, cat):
        return Product.objects \
            .filter(is_visible=True) \
            .filter(taxonomy__0=cat) \
            .order_by('rand2') \
            .all()[:self.product_limit]


class CategoryView(ListView):
    context_object_name = 'products'
    model = Product
    ordering = '-created'
    paginate_by = 12
    template_name = 'web/home.html'

    def dispatch(self, *args, **kwargs):
        self.cat_id = self.kwargs['cat']
        self.cat_name = CAT_NAME_LOOKUP.get(self.cat_id)

        if self.cat_id not in CAT_NAME_LOOKUP:
            return redirect('web:home')

        return super(CategoryView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset() \
            .filter(is_visible=True) \
            .filter(taxonomy__0=self.cat_name) \
            .order_by('rand2')

        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)

        context.update({
            'category': {
                'id': self.cat_id,
                'display': self.cat_name,
            },
        })

        return context
