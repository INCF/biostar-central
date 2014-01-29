from django.conf import settings

from celery import task
from django.core.mail import send_mail
from django.contrib.sites.models import Site
import markdown2x
from main.server import autolink
from main.server.html import unicode_or_bust, strip_tags
from main.server import notegen
from django.core.mail import EmailMultiAlternatives

# import all constants
from main.server.const import *

@task
def demo_add(x, y):
    return x + y

@task
def send_test_email():
    subject = "test email"
    sender  = "istvan.albert@gmail.com"
    recipient = "iua1@psu.edu"
    body = "this is a test email"

    print "sending test email"

    #send_mail(subject, body, sender, [recipient], fail_silently=False)

@task
def send_email_note(sender, target, content, type=NOTE_USER, date=None, url=''):
    """
    Sends an email notification for a note. 
    """

    md = markdown2x.Markdown(safe_mode=False, extras=["code-friendly", "link-patterns"],
                             link_patterns=autolink.patterns)

    # get html content
    content_md = md.convert(content)
    content_html = unicode_or_bust(content_md)

    # parse internal links to contain the domain name, explicitly not using regex for speedup
    content_html_split = content_html.split("<a href='/")
    content_html = ("<a href='http://" + settings.SITE_DOMAIN + "/").join(content_html_split)
    
    subject = notegen.email_subject(type)
    sender  = settings.DEFAULT_FROM_EMAIL
    recipient = target.email

    #print "sending email notice to %s: \n %s \n %s" % (target.email, subject, content_html)
    # prepare multipart message and send
    msg = EmailMultiAlternatives(subject, strip_tags(content_html), sender, [recipient])
    msg.attach_alternative(content_html, "text/html")
    msg.send()
    
if __name__ == '__main__':
    send_test_email()
