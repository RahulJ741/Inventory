from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^add_group/$',add_group, name='add_group'),
    url(r'^home/$',home, name='home'),
]
