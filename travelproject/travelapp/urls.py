from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.demo,name='demo'),
    #path('addition/',views.addition,name='addition'),
    #path('contact/',views.contact,name='contact'),
    #path('detail/',views.detail,name='detail'),
    #path('thanks/',views.thanks,name='thanks')
]