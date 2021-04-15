#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from coverage import Coverage

from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'numerated.settings')

    try:
        command = sys.argv[1]
    except IndexError:
        command = "help"

    running_tests = (command == 'test')
    if running_tests:
        cov = Coverage()
        cov.erase()
        cov.start()

    execute_from_command_line(sys.argv)

    if running_tests:
        cov.stop()
        cov.save()
        covered = cov.report()
        if covered < 100:
            sys.exit(1)

if __name__ == '__main__':
    main()
