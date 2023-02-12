from django.db import models

# Create your models here.


class student_details(models.Model):
    std_id=models.CharField(max_length=260,primary_key=True)
    name = models.CharField(max_length=260)
    std_age = models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    phone=models.PositiveSmallIntegerField()
    email=models.EmailField()