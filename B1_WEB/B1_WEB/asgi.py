"""
ASGI config for B1_WEB project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file_task, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'B1_WEB.settings')

application = get_asgi_application()
