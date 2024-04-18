from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """
    Model representing user profile information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        String representation of the profile, returns the username followed by 'Profile'.
        """
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Override the save method to resize profile images.
        """
        super().save(*args, **kwargs)  

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Post(models.Model):
    """
    Model representing a post.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the post, returns the title.
        """
        return self.title