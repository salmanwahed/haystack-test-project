# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from noticeboard import views

urlpatterns = [
    url(r'^$', views.testing_view),
]