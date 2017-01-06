import logging

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
import mailchimp


logger = logging.getLogger(__name__)


class NewsletterView(View):
    def post(self, request):
        email = request.POST.get('email')

        try:
            self.subscribe(email)
            status = 'success'
        except mailchimp.ListAlreadySubscribedError:
            status = 'success'
        except Exception as e:
            logger.warning('error subscribing to newsletter: {}'.format(e))
            status = 'success'

        return JsonResponse({'status': status})

    def subscribe(self, email):
        m = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
        m.lists.subscribe(
            settings.MAILCHIMP_LIST_ID,
            {'email': email},
            double_optin=False
        )
