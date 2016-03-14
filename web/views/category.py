from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView

from web.models import Product
from web.util.categories import CATEGORIES


class CategoriesView(TemplateView):
    template_name = 'web/categories.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['categories'] = CATEGORIES
        return context


class CategoryView(ListView):
    context_object_name = 'products'
    model = Product
    ordering = '-created'
    paginate_by = 12
    template_name = 'web/home.html'

    def dispatch(self, *args, **kwargs):
        self.category = self.kwargs['cat']
        if self.category not in CATEGORIES:
            return redirect('web:home')
        return super(CategoryView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        return qs.filter(category=CATEGORIES[self.category])
