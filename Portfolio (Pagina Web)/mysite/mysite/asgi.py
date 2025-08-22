"""
ASGI config for mysite project.
"""

import os
from django.core.asgi import get_asgi_application

# CORRECCIÓN CLAVE: La ruta correcta al módulo de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')

application = get_asgi_application()