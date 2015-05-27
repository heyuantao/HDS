from django.db import models

# Create your models here.
class Response_By_Keywords_Model(models.Model):
    keywords=models.TextField();
    response=models.TextField();
