import os
import settings
import logging
from django.http import HttpResponse
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin

import infochimpy

admin.autodiscover()

def home(request):
    ''' Returns a Trstrank result. 
        Defaults to settings.py if no args'''
    
    data = request.GET.copy()
        
    if not data.get("screen_name"):
        chimps = infochimpy.api.trstrank(settings.INFOCHIMPS_SCREEN_NAME, settings.INFOCHIMPS_API_KEY)
    else:
        screen_name = data.get("screen_name")
        if screen_name[0] == '@':
            screen_name = screen_name[1:]
        chimps = infochimpy.api.trstrank(screen_name, settings.INFOCHIMPS_API_KEY)
        
    return direct_to_template(request, "homepage.html",
            {   'quotient' : chimps.values()[3],
                'rank' : chimps.values()[2],
                'screen_name': chimps.values()[1],
                'STATIC_URL': settings.STATIC_URL,
            })

urlpatterns = patterns('',
    (r'^$', home),
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)