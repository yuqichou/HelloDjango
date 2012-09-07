import os
import sys

path = 'D:/workspace/indigo/HelloDjango'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'HelloDjango.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()