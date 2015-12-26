from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^message/' , include('message.urls')),
    url(r'^app/', include('accounts.urls')),
    ]