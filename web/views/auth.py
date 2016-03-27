from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView, View


class SignupView(TemplateView):
    template_name = 'web/auth.html'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Join Uncoverly',
            'headline': 'Sign up to like and add products.',
            'btn_verb': 'Connect',
        })
        return context


class LoginView(TemplateView):
    template_name = 'web/auth.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Log in',
            'headline': 'Welcome back.',
            'btn_verb': 'Log in',
        })
        return context


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('web:home')
