from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'web/about.html'
    products = [
        {
            'id': '210486081',
            'img': 'https://img0.etsystatic.com/048/2/10209273/il_340x270.679851814_5mhc.jpg'
        },
        {
            'id': '105743280',
            'img': 'https://img0.etsystatic.com/030/0/6380054/il_340x270.644529370_h2xq.jpg'
        },
        {
            'id': '212532937',
            'img': 'https://img1.etsystatic.com/047/1/7859729/il_340x270.687813701_2tse.jpg'
        },
        {
            'id': '215232318',
            'img': 'https://img0.etsystatic.com/053/0/7896075/il_340x270.699001072_oyvb.jpg'
        },
        {
            'id': '239600689',
            'img': 'https://img0.etsystatic.com/133/0/10146012/il_340x270.995024864_4x88.jpg'
        },
        {
            'id': '189611317',
            'img': 'https://img0.etsystatic.com/040/1/5255767/il_340x270.602353910_k5cr.jpg'
        },
    ]

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        context.update({
            'banner': self.products[:4],
            'p1': self.products[-2],
            'p2': self.products[-1],
        })

        return context
