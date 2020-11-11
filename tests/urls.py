#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create: 2020-11-11 13:25:56
# LastEdit: 2020-11-11 15:10:43
"""说明暂无"""
__author__ = '749B'


from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django_ipam import views

urlpatterns = [
    url(r'^', include('django_ipam.urls', namespace='ipam')),
    url(r'^admin/', admin.site.urls),
    path('', views.hello),
]
