from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    """user profile"""

    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(upload_to="profile_pics")


class Blog(models.Model):
    """blog objects"""

    author = models.ForeignKey(
        User, related_name="post_author", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, verbose_name="Put a title")
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(verbose_name="What is on your mind?")
    image = models.ImageField(upload_to="blog_images")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """comment objects"""

    blog = models.ForeignKey(
        Blog, related_name="blog_comment", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="user_comment", on_delete=models.CASCADE
    )
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Likes(models.Model):
    """likes objects"""

    blog = models.ForeignKey(Blog, related_name="liked_blog", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="liked_user", on_delete=models.CASCADE)
