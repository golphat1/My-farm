from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Defining the Post model, inheriting from Django's Model class
class Post(models.Model):
    # Field for the title of the post, limited to 100 characters
    title = models.CharField(max_length=100)
    
    # Field for the content of the post, allowing for longer text
    content = models.TextField()
    
    # Field for the date and time when the post was created, with default value set to the current time
    date_posted = models.DateTimeField(default=timezone.now)
    
    # Field representing the author of the post, linked to the User model, with CASCADE delete behavior
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    # String representation of the Post object, returning its title
    def __str__(self):
        return self.title

    # Method to get the absolute URL of the post detail page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
