from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.shortcuts import redirect

from web.models import Find


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
        qs = super(FindsView, self).get_queryset()
        return qs.filter(user_id=self.owner_id)

    def get_context_data(self, **kwargs):
        context = super(FindsView, self).get_context_data(**kwargs)
        context['owner'] = self.owner
        return context


class FindView(View):
    template_name = 'web/find.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if not request.user.is_authenticated():
            return self.outcome(status='fail', reason='no_auth')

        post = request.POST
        print(post)

        return self.outcome(status='incomplete')

    def outcome(self, **kwargs):
        return JsonResponse(dict(**kwargs))
