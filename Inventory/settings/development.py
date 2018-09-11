from .base import *

DEBUG = True

Mysql_user = 'to_all'
Mysql_pass = '123456789'
MyDefaultHost = 'localhost'


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


ALLOWED_HOSTS = ['10.200.234.101','localhost','127.0.0.1']

# The URL where requests are redirected for login, especially when using the login_required() decorator.
LOGIN_URL = "/"

#LOGIN_URL counterpart.
LOGOUT_URL = "/logout/"
