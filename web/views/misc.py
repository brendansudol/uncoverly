from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'web/contact.html'


class PrivacyView(TemplateView):
    template_name = 'web/privacy.html'


class TermsView(TemplateView):
    template_name = 'web/terms.html'
