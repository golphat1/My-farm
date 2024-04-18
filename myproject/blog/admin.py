from django.contrib import admin
from .models import Post # Importing the Post model from the current directory's models module

admin.site.register(Post) # Registering the Post model with the admin site