from django.views.generic import ListView

from web.models import Find


class FindsView(ListView):
    context_object_name = 'finds'
    model = Find
    ordering = '-created'
    paginate_by = 25
    template_name = 'web/finds.html'

    def get_queryset(self):
        qs = super(FindsView, self).get_queryset()
        return qs.filter(user_id=self.request.user.pk)
