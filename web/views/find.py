import re

from urllib.parse import urlparse

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import redirect

from web.models import Find, Product


class FindsView(ListView):
    context_object_name = 'finds'
    model = Find
    ordering = '-created'
    paginate_by = 12
    template_name = 'web/finds.html'

    def dispatch(self, *args, **kwargs):
        self.owner_id = self.kwargs['uid']
        try:
            self.owner = User.objects.get(pk=self.owner_id)
        except Exception:
            return redirect('web:home')
        return super(FindsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(FindsView, self).get_queryset() \
            .filter(user_id=self.owner_id) \
            .filter(product__image__isnull=False)

        return qs

    def get_context_data(self, **kwargs):
        context = super(FindsView, self).get_context_data(**kwargs)
        context['owner'] = self.owner
        return context


class FindView(View):
    template_name = 'web/find.html'

    def get(self, request):
        return render(request, self.template_name)

    # TODO - clean up, this is quite clunky
    def post(self, request):
        if not request.user.is_authenticated():
            return self.outcome('fail', reason='no_auth')

        url = request.POST.get('url')
        parsed = urlparse(url)

        if parsed.netloc != 'www.etsy.com':
            return self.outcome('fail', reason='not_etsy')

        m = re.search('www.etsy.com\/listing\/(\d+)', url)
        if m is None:
            return self.outcome('fail', reason='no_product')

        pid = m.group(1)
        p = Product.objects.filter(pk=pid).first()

        if p and p.is_visible:
            return self.outcome('already_live')

        if p and p.finds.first():
            return self.outcome('already_suggested')

        if not p:
            p = Product.objects.create(id=pid)

        Find.objects.create(user=request.user, product=p)
        return self.outcome('success')

    def outcome(self, status, **kwargs):
        return JsonResponse(dict(status=status, **kwargs))
