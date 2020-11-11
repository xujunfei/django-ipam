#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create: 2020-11-11 16:01:53
# LastEdit: 2020-11-11 16:09:40
"""说明暂无"""
__author__ = '749B'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'line_num': {
            'format': '{name}[{lineno:d}]: {message}',
            'style': '{',
        },
        'line_num_level': {
            'format': '{name}[{lineno:d}]: [{levelname}]{message}',
            'style': '{',
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'line_num'
        },
        'console_backend': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'line_num_level'
        },
        'console_utils': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'line_num_level'
        },
    },
    'loggers': {
        'django_ipam.views': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
        },
    }
}
