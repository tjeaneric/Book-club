from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=100)
    description = RichTextField()
    read_by = models.DateField()




class Discussion(models.Model):
    book = models.ForeignKey('Book', related_name='discussion', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)
    opinion = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True)

