import mailchimp

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View


class NewsletterView(View):
    def post(self, request):
        email = request.POST.get('email')

        try:
            self.subscribe(email)
            outcome = 'success'
        except mailchimp.ListAlreadySubscribedError:
            outcome = 'already_member'
        except Exception:
            outcome = 'error'

        return JsonResponse({'outcome': outcome})

    def subscribe(self, email):
        m = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
        m.lists.subscribe(
            settings.MAILCHIMP_LIST_ID,
            {'email': email},
            double_optin=False
        )
