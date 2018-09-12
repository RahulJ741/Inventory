# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'home.html')


def add_group(request):
    return HttpResponse('asdfasdfasdfasdfasdfasdfasdfasd')

@csrf_exempt
def home_url(request):
    login = Login_handle()
    if request.method == 'GET':
        return login.render_template(request, 'signin.html')
    elif request.method == 'POST':
        return login.login(request)


def logout_user(request):
    try:
        login = Login_handle()
        return login.logout_user(request)

    except Exception as e:
        print "Exception occured in logout_user ",e
        return HttpResponse(status=500)



class Login_handle(object):
    """docstring for Login_handle. class that handles all the login functionalty"""
    # def __init__(self):
        # self.form = LoginForm()
    #     super(Login_handle, self).__init__()
    #     self.arg = arg


    def render_template(self, request, template_name):
        return render_to_response(template_name)

    def login(self, request):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        remember_me = request.POST.get('remember_me',None)

        if username != None and password != None:
            # print username,password, ":;;;;;;;;;;;;;;;;;;;;;;;;//////////////////////////"
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                print ":::::::::::>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                login(request, user)
                return HttpResponseRedirect('/login_path/home/')
                # return render(request,'home.html')
            else:
                return render_to_response('Error.html',{'Error_title':'User not found','Error_message': 'Username or password incorrect'})

    def logout_user(self, request):
        try:
            logout(request)
            return HttpResponseRedirect('/')
        except Exception as e:
            print "Exception occured in logout_user ............ ",e
            return HttpResponse(status=500)
