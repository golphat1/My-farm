from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    AppConfig subclass for configuring the 'users' app.
    """

    name = 'users'

    def ready(self):
        """
        Method called when the application is ready.
        Import signals module to ensure signals are registered.
        """
        import users.signals
