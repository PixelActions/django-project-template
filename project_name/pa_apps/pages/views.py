from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
#from contact_form.views import ContactFormView
from django import forms
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import  select_template

class HomeView(TemplateView):
    template_name = "pages/home.html"

class TemplateLocatorView(TemplateView):
    subfolder = "" #Use if templates are placed in a subfolder
    template_name = "" #Overwrite on url structure
    def get_template_names(self):
        template_name = self.kwargs['page_template_name']
        template_name = template_name.replace('.','')
        template_name = template_name.replace('/','')
        if self.subfolder:
            return ["pages/%s/%s.html" % (self.subfolder,template_name)]
        else:
            return ["pages/%s.html" % template_name]
    def render_to_response(self, context, **response_kwargs):
        try:
            template = select_template(self.get_template_names())
            return super(TemplateLocatorView, self).render_to_response(context,**response_kwargs)
        except TemplateDoesNotExist:
            raise Http404

'''
class ContactView(ContactFormView):
    template_name = 'pages/contact.html'
    #If the form is saved successfully, a messages.success is being sent, else a messages.error.
    #Override the defaults for custom messages:

    #form_valid_message = settings.CONTACT_FORM_VALID_MESSAGE
    #form_invalid_message = settings.CONTACT_FORM_INVALID_MESSAGE
'''