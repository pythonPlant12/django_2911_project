from django.db import models

# Create your models here.
class BookModel(models.Model):
  name = models.CharField(max_length=255)
  author = models.ForeignKey('authors.AuthorModel', on_delete=models.CASCADE)