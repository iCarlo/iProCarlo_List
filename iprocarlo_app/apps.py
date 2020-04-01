from django.apps import AppConfig


class IprocarloAppConfig(AppConfig):
    name = 'iprocarlo_app'

    def ready(self):
        import iprocarlo_app.signals
