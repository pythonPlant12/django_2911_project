from django.db import models

class AuthorModel(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)

  def __str__(self):
    return self.name + self.surname

  class Meta:
    managed = True