# -*- coding: utf-8 -*-
'''
Created on Sep 6, 2012
@author: YuqiChou
'''
from HelloDjango import settings

def global_list_per_page(context):
    
    return {'GLOBAL_LIST_PER_PAGE': settings.GLOBAL_LIST_PER_PAGE,
            'GLOBAL_PAGE_PER_VIEW': settings.GLOBAL_PAGE_PER_VIEW}