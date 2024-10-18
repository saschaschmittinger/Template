from django.shortcuts import render
from django.views import generic
from product.models import Product



class FrontPageView(generic.ListView):
    title = 'SSC E-Commerce'
    queryset = Product.objects.all()[0:8]
    template_name = 'core/index.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super(FrontPageView, self).get_context_data(**kwargs)  
        context.update({'title': self.title})  
        return context



class ShopPageView(generic.ListView):
    title = 'SSC Shop'
    queryset = Product.objects.all()
    template_name = 'shop/shop_list.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super(ShopPageView, self).get_context_data(**kwargs)  
        context.update({'title': self.title})  
        return context
    


class ShopDetailView(generic.DetailView):
    title = 'SSC Detail View'
    queryset = Product.objects.all()
    context_object_name ='product'
    
    def get_context_data(self, **kwargs):
       context = super(ShopDetailView, self).get_context_data(**kwargs)  
       context.update({'title': self.title})  
       return context