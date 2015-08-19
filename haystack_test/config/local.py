# -*- coding: utf-8 -*-

from settings import *

DEBUG = True

if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar',
    ]
