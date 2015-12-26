from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'dash', views.dash, name='dash'),
    url(r'mess',views.mess , name='mess'),
    url(r'send', views.send , name ='send'),
    url(r'logout' , views.logout , name = 'logout'),
    url(r'newmes' , views.newmes , name = 'newmes'),
    url(r'create' , views.create , name = 'create'),
]