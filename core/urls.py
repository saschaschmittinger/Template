from django.urls import path
from .views import FrontPageView, ShopPageView

app_name = 'core'

urlpatterns = [
    path('', FrontPageView.as_view(), name='index_view'),
    path('shop/', ShopPageView.as_view(), name='shop_view'),
]
