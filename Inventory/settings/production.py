from .base import *

DEBUG = False

Mysql_user = 'to_all'
Mysql_pass = '123456789'
MyDefaultHost = 'localhost'
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'matchsitedb_r&d',                      # Or path to database file if using sqlite3.
        'USER': Mysql_user,
        'PASSWORD': Mysql_pass,
        'HOST': MyDefaultHost,
        'PORT': '',                      # Set to empty string for default.
    },
}
