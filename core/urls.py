from django.urls import path
from .views import FrontPageView 

app_name = 'core'

urlpatterns = [
    path('', FrontPageView.as_view(), name='index_view'),
 
]
