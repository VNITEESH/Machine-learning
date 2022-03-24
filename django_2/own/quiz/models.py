from django.db import models
from datetime import date
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import ForeignKey
class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(date.today())
    
    def __str__(self):
        return self.question_text
# Create your models here.
class Choices(models.Model):
    Questions =models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    