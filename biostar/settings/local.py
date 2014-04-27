# -*- coding: utf8 -*-
#
# Django settings for biostar project.
#

# Extend base settings
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env("DATABASE_NAME"),
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': get_env("PG_PORT_5432_TCP_ADDR"),
        'PORT': get_env("PG_PORT_5432_TCP_PORT"),
    }
}
