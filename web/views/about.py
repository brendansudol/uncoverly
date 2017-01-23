from django.views.generic import TemplateView

from web.models import Product


class AboutView(TemplateView):
    template_name = 'web/about.html'
    pids = [
        '210486081', '216832109', '212532937',
        '215232318', '61236827', '193883166',
    ]

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        data = {p.pk: p for p in Product.objects.filter(pk__in=self.pids)}

        context.update({
            'banner': [data[id] for id in self.pids[:4]],
            'p1': data[self.pids[-2]],
            'p2': data[self.pids[-1]],
        })

        return context
