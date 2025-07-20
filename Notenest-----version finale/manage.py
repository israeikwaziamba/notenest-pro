#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notenest_pro.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django n'est pas installé ou le chemin des modules est incorrect. "
            "Assure-toi d'avoir activé ton environnement virtuel et installé Django."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '_main_':
    main()