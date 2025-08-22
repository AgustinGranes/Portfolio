#!/usr/bin/env python
"""
manage.py
Script de utilidad para la gestión de Django.
"""
import os
import sys

def main():
    # CORRECCIÓN CLAVE: La ruta correcta al módulo de configuración
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y disponible en tu entorno?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()