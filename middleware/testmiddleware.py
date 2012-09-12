# -*- coding: utf-8 -*-
'''
Created on Sep 12, 2012
@author: YuqiChou
'''

class TestMiddleware(object):

    def process_request(self,request):
        pass
    
    def process_response(self, request, response):
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass
    
    def process_template_response(self, request, response):
        pass
    
    def process_exception(self, request, exception):
        pass