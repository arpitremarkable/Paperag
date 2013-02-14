#!/usr/bin/env python
import os
import sys
from live_stylus import ConvStylus
import subprocess

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Paperag.settings")

    ConvStylus()
    #subprocess.call(["stylus", "-w", "nonApps/static/templates/"])
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
