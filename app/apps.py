from django.apps import AppConfig

# where we configure the app for the project
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


    # registering signals to the app
    def ready(self):
        import app.signals