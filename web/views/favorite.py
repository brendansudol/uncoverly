from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView, View

from web.models import Favorite


class FavoritesView(ListView):
    context_object_name = 'faves'
    model = Favorite
    ordering = '-updated'
    paginate_by = 25
    template_name = 'web/faves.html'

    def get_queryset(self):
        qs = super(FavoritesView, self).get_queryset()
        return qs.filter(user_id=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        context['user'] = User.objects.get(pk=1)  # FIXME
        return context


class FavoriteView(View):
    def post(self, request, pid):
        if not request.user.is_authenticated():
            return self.outcome(status='fail', reason='no_auth')

        condits = {
            'user_id': request.user.pk,
            'product_id': pid
        }

        fave = Favorite.objects.filter(**condits).first()

        if not fave:
            Favorite.objects.create(**condits)
            return self.outcome(status='success', action='add')
        else:
            fave.delete()
            return self.outcome(status='success', action='remove')

    def outcome(self, **kwargs):
        return JsonResponse(dict(**kwargs))
