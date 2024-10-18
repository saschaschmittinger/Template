from django.shortcuts import render
from django.views import generic


class FrontPageView(generic.TemplateView):
    title = 'SSC E-Commerce'
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)  
        context.update({'title': self.title})  
        return context
