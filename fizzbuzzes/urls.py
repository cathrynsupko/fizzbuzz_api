from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^fizzbuzz/$', views.fizzbuzz_list),
  url(r'^fizzbuzz/(?P<pk>[0-9]+)/$', views.fizzbuzz_detail)
]