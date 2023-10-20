from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=233)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=233)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=220, default='coding')
    snippet = models.CharField(max_length=220, default='Click the Above to Read Blog Post...')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
    # def __str__(self):
        # return self.title + '|' + str(self.author)

    # def get_absolute_url(self):
        # return reverse('home')
        # return reverse("article-details", args=(str(self.id)))
