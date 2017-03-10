from django.views.generic import TemplateView

from web.models import Product


class ContactView(TemplateView):
    template_name = 'web/contact.html'


class LabsView(TemplateView):
    template_name = 'web/labs.html'

    def get_context_data(self, **kwargs):
        context = super(LabsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(is_visible=True).all()[:9]
        return context


class PrivacyView(TemplateView):
    template_name = 'web/privacy.html'


class QuizView(TemplateView):
    template_name = 'web/quiz.html'


class TermsView(TemplateView):
    template_name = 'web/terms.html'
