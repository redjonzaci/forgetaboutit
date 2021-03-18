from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Blogger(models.Model):
    """Model representing a blogger."""
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=200, help_text="Enter your bio details here.")

    class Meta:
        ordering = ['user', 'bio']

    def get_absolute_url(self):
        """Return URL to access a Blogger instance."""
        return reverse('blogger', args=[str(self.id)])

    def __str__(self):
        """String representing a blogger."""
        return self.user.username


class Post(models.Model):
    """Model representing a post."""
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Blogger, on_delete=models.RESTRICT)
    description = models.TextField(help_text="Enter your thoughts here.")
    post_date = models.DateTimeField(default=timezone.localtime)

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """Return URL to a post."""
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """String representing a post."""
        return self.title


class Comment(models.Model):
    """Model representing a comment on a post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    description = models.TextField(
        max_length=200, help_text="Enter your comment here.")
    post_date = models.DateTimeField(default=timezone.localtime)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        """String for representing a comment."""
        len_title = 50
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + "..."
        else:
            titlestring = self.description
        return titlestring
