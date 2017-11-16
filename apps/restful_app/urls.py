from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/add$', views.new),
    url(r'^users/added$', views.add),
    url(r'^users/(?P<number>\d+)/show$', views.show),
    url(r'^users/(?P<number>\d+)/delete$', views.delete),
    url(r'^users/(?P<number>\d+)/edit$', views.abouttoedit),
    url(r'^users/(?P<number>\d+)/doneedit$', views.edit),
]
