"""
MBTA Config
"""
from django.apps import AppConfig


class MBTAConfig(AppConfig):
    """MBTA Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mbta'

    api_key = '9ece9f6f38854ba9aec68e6912b764db'
