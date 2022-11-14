from django.db import models

# Create your models here.
# Author
class Author(models.Model):
  first_name= models.CharField(max_length=255)
  last_name= models.CharField(max_length=255)
  username= models.CharField(max_length=255)
  description= models.TextField(null=True, blank=True)
  email = models.EmailField()
  phone = models.CharField(max_length=255)
  created_at = models.DateField(auto_now_add=True)

# Category
class Category(models.Model):
  title= models.CharField(max_length=255)

# Story
class Story(models.Model):
  description= models.TextField(null=True, blank=True)
  title= models.CharField(max_length=500)
  author= models.ForeignKey(Author, on_delete=models.CASCADE)
  created_at= models.DateField(auto_now_add=True)
# Chapter
class Chapter(models.Model):
  title= models.CharField(max_length=500)
  story= models.ForeignKey(Story, on_delete=models.CASCADE)
  created_at= models.DateField(auto_now_add=True)
