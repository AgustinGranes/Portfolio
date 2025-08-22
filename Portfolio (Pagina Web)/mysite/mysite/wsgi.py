"""
WSGI config for mysite project.
"""

import os
from django.core.wsgi import get_wsgi_application

# CORRECCIÓN CLAVE: La ruta correcta al módulo de configuración
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')

application = get_wsgi_application()

# Esto es requerido por Vercel
app = application