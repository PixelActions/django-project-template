from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from contact_form.views import ContactFormView
from django import forms


    
class AboutView(TemplateView):
    template_name = "pages/about.html"
 
class TermsView(TemplateView):
    template_name = "pages/terms.html"
class DisclaimerView(TemplateView):
    template_name = "pages/disclaimer.html"

class ContactView(ContactFormView):
    template_name = 'pages/contact.html'
    #If the form is saved successfully, a messages.success is being sent, else a messages.error.
    #Override the defaults for custom messages:
    
    #form_valid_message = settings.CONTACT_FORM_VALID_MESSAGE
    #form_invalid_message = settings.CONTACT_FORM_INVALID_MESSAGE