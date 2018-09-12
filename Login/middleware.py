from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import *
from Inventory import constants
# import inspect

class InventoryMiddleware(object):
    """docstring for InventoryMiddleware. middleware for inventory that check the request type and grants or rejects data to that particular requests"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        data = self.process_request(request)
        return data


    def process_request(self, request):
        print "in process_view //////////////"
        print request.method, "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
        # print inspect.stack()[1][3], "0000000000000000000000 gets the caller funtion ie __call__ for this case"
        # print request

        if request.method == 'GET':
            request_data = self.get_response(request)
            return request_data
        else:
            # request_data = self.get_response(request)
            print request.user ,"...................................."
            return self.check_user_rights(request)
            # return request_data
            # return HttpResponseForbidden('You are not authorized to rebuild builds')


    def check_user_rights(self, request):
        request_data = self.get_response(request)
        # print request.resolver_match.url_name,"oopopopo"
        if request.resolver_match.url_name in constants.POST_Request_Excempt_Urls:
            print True, "123456789"
            return request_data
        else:
            roles_list = UsersRights.objects.filter(user = request.user)
            print roles_list ,":.;.;.;.;;.;;.;.;.;.;.;.;.;.;.;.;.;."
            return request_data
