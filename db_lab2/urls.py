from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_posts, name='all_posts'),
    ]
