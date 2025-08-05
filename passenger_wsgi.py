# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/m/maylun0m/medkhan/Medkhan')
sys.path.insert(1, '/home/m/maylun0m/medkhan/Medkhan/venv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Medkhan.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()