#!/usr/bin/env python

import os
import sys
import dotenv

from django.contrib.staticfiles import finders
from django.conf import settings


if __name__ == "__main__":
    dotenv.read_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "blog.settings.prod_settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
