"""
All the Configuration for the Login Application is written here
"""
from django.apps import AppConfig


class LoginConfig(AppConfig):
    """
    Logic for the Login Application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Login'
