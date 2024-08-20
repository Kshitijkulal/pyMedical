from django.db import models

# Create your models here.
class Patient(models.Model):
    choices = [('M', "male"),
               ('F', "female")]
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=1, choices=choices)
    disease=models.CharField(max_length=200)

    def __str__(self):
      return self.name