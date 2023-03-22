from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from api.models import Form
        Form.create_default_forms()


"""
class ApiConfig(AppConfig):
    name = 'api'
"""
