from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # todo => connecting signals file, so it will work
    def ready(self):
        import users.signals
