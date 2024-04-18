from django.apps import AppConfig

# Defining a custom AppConfig for the 'blog' app
class BlogConfig(AppConfig): # Specifies the default primary key field for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog' # Specifies the name of the app
