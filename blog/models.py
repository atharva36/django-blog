from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        # return reverse('articleDetail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField()
    # body = models.TextField()
    category = models.CharField(max_length=255,default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('articleDetail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=160)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)

    class Meta:
        ordering = ['-date_added']