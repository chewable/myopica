import os, sys

sys.path.append('/var/www/myopica/')
sys.path.append('/var/www/myopica/myopica/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'myopica.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
