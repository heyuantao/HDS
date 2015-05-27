import os
#import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'HDS.settings'
#application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
