"""
All the Configuration for the User Profile Application is written here
"""
from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    """
    Configuration for the User Profile Application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'
