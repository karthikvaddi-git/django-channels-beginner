"""
ASGI config for channelproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application

from django.core.asgi import get_asgi_application
from django.urls import path
from asgiref.sync import async_to_sync
from home.consumers import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelproject.settings')

application = get_asgi_application()
ws_pattern=[path('home/',testconsumer.as_asgi())]
application=ProtocolTypeRouter({
    'websocket':URLRouter(ws_pattern)
})