from django.conf.urls import url, include
from Login.views import *

urlpatterns = [
    url(r'^add_group$',add_group, name='add_group'),
]
