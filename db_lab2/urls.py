from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^click$', views.click, name='click'),
    url(r'^ShowCompanies$', views.showcompanies, name='ShowCompanies'),
    ]
