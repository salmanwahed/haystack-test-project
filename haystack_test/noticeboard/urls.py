# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from noticeboard.views import NoticeBoardView

urlpatterns = [
    url(r'^$', NoticeBoardView.as_view(), name='notice-board'),
]