"""
ASGI config for ms4_riss_jewels_and_designs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ms4_riss_jewels_and_designs.settings")

application = get_asgi_application()
