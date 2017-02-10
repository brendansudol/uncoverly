from urllib.parse import unquote_plus

from django.shortcuts import redirect
from django.views.generic import ListView

from web.models import Product


class SearchView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 12
    template_name = 'web/search.html'

    def dispatch(self, *args, **kwargs):
        q = self.request.GET.get('q')

        if not q:
            return redirect('web:home')

        self.query = q
        self.query_clean = unquote_plus(q)

        return super(SearchView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = self.model.objects.search(self.query_clean) \
            .filter(is_visible=True) \
            .order_by('-rand2')

        return qs

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        context.update({
            'query': self.query,
            'query_clean': self.query_clean,
            'total': self.get_queryset().count(),
        })

        return context
