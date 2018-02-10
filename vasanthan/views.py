from django.http import request
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import redirect
import logging
# Create your views here.
from django.template import RequestContext, Template
from django.views import defaults
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
from django.views.generic import TemplateView
from vasanthan.forms import ContactMeFrom

logger = logging.getLogger (__name__)


class HomePageView (TemplateView):
    template_name = 'index.html'


# @ensure_csrf_cookie
@csrf_protect
def render_contact_page(request):
    contact_from = ContactMeFrom
    template_name = 'contact.html'
    if request.method == 'GET':
        my_data_dictionary = {'form': contact_from}
        return render (request, template_name, my_data_dictionary)


@csrf_exempt
def send_mail_local(request):
    template_name = 'contact.html'
    success_message_template = 'success_message.html'
    contact_from = ContactMeFrom

    @csrf_protect
    def protected(request):
        logger.error ("sdvdfvfvdf")
        logger.error (request.method)
        if request.method == 'POST':
            logger.error (request.POST.dict ())
            form = contact_from (data=request.POST)
            logger.error (form.is_valid ())
            if form.is_valid ():
                logger.error ("hhheyyy it came")
                contact_name = request.POST.get (
                    'contact_name'
                    , '')
                contact_email = request.POST.get (
                    'contact_email'
                    , '')
                form_content = request.POST.get ('content', '')
                logger.error (form_content)
                # template = render_to_string('contact_template.html')
                context = {
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                }
                content = render_to_string ('contact_template.html', context)

                email = EmailMessage (
                    "New contact form submission",
                    content,
                    "vinnarasan.c@gmail.com" + '',
                    ['vasanthan93c@gmail.com'],
                    headers={'Reply-To': contact_email}
                )
                email.send ()
                logger.error ("EMAIL SENT")
                # return redirect('/')

    protected (request)
    # return JsonResponse ({'message': 'mail sent successfully'})
    return render (request, success_message_template)


class AboutMePageView (TemplateView):
    template_name = 'about.html'
