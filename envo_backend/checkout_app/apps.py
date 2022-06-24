"""
All the Configuration for the Checkout Application is written here
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Logic for the Checkout Application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout_app'
