from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Once the post is stored in the db, it tries to show the detailed view of that post.
    # We need to define this method so that django knows how to find a location of specific post.

    # Redirect vs Reverse
        # Redirect just redirects whereas reverse will return the URL as a string & view hanldes redirect.
    def get_absolute_url(self):                                         
        return reverse('post-detail', kwargs={'pk': self.pk})
        # return reverse('blog-home');