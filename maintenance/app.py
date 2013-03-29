'''
Created on Mar 29, 2013

@author: asseym
'''
# -*- coding: utf-8 -*-
import rapidsms
import datetime

from rapidsms.apps.base import AppBase
from rapidsms_httprouter.models import Message
from django.conf import settings 

class App(AppBase):

    def handle (self, message):
        # if UNDER_MAINTENANCE flag is set 
        if settings.UNDER_MAINTENANCE:
            message.respond('We have noted your message. This service is under scheduled maintenance please check later.')
            return True
        
        return False