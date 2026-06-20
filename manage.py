#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# uv sync
# cp .env.example .env
# uv run python manage.py migrate
# uv run python manage.py createsuperuser
# uv run python manage.py runserver