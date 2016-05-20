from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    url(r'^click$', views.click, name='click'),
    url(r'^ShowCompanies$', views.showcompanies, name='ShowCompanies'),
    url(r'^ShowAllInfo$', views.showallinfo, name='ShowAllInfo'),
    url(r'^ShowEmployeeInfo$', views.showemployeeinfo, name='ShowEmployeeInfo'),
    url(r'^ShowWorkPlace$', views.showworkplace, name='ShowWorkPlace'),
    url(r'^Accounting$', views.accounting, name='Accounting'),
    url(r'^Addvisiting', views.addvisiting, name='Accounting'),

    #url(r'^Accounting/GetId$', views.GetId, name='Accounting'),
    ]
