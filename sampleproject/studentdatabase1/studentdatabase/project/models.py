from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


