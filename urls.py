from django.conf.urls import url
from . import views


urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



    url(r'bookForm/$', views.bookForm, name='bookForm'),

    url(r'', views.index, name='index'),
    ]
