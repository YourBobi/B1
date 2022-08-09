"""
WSGI config for B1_WEB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file_task, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'B1_WEB.settings')

application = get_wsgi_application()
