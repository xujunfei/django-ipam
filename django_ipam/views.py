#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create: 2020-11-11 15:07:55
# LastEdit: 2020-11-11 16:12:29
"""说明暂无"""
__author__ = '749B'


from django.shortcuts import render, HttpResponse

import logging

logger = logging.getLogger(__name__)

def hello(request):
    logger.debug("%s 请求了默认的首页" % request.META.get('REMOTE_ADDR', 'UnknownRemote'))
    resp = """<h1><a href="/admin">转到 Django Admin</a></h1>"""
    return HttpResponse(resp)