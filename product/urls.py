from django.urls import path
from core.views import FrontPageView, ShopPageView, ShopDetailView

app_name = 'product'

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name='shop_view'),
    path('shop/<slug:slug>', ShopDetailView.as_view(), name='shop_detail')
]
