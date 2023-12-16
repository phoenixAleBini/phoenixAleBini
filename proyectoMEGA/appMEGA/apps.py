from django.apps import AppConfig


# requisito para signals.py

class AppMEGAConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appMEGA'

    def ready(self):
        import appMEGA.signals  