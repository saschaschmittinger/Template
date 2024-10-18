from django.shortcuts import render
from django.views import generic
from product.models import Product


class FrontPageView(generic.ListView):
    title = 'SSC E-Commerce'
    queryset = Product.objects.all()
    template_name = 'core/index.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)  
        context.update({'title': self.title})  
        return context
