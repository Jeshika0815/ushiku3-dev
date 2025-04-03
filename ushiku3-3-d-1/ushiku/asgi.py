"""
ASGI config for ushiku project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

#import apps routing
import home.routing
import sagyoshiji.routing
import sagyodenpyo.routing
import docs.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ushiku.settings')

"""
class WebSocketPathFilteerMiddleware:
    #特定のページ・サイトでのWebSocketの適応を外す
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "websocket":
            path = scope["path"]
        
        #Websocketを無効化にするアプリケーション
        excluded_paths = [
            "/ws/no-socket-docs",
        ]

        if path in excluded_paths:
            await send({"type": "websocket.close"})
            return
        
        #通常の処理
        await self.app(scope, receive, send)
"""

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                home.routing.websocket_urlpatterns +
                sagyoshiji.routing.websocket_urlpatterns +
                sagyodenpyo.routing.websocket_urlpatterns +
                docs.routing.websocket_urlpatterns 
            )
        ),
    }
)
