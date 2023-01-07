from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200,)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    course = models.ManyToManyField(Course,)


    def __str__(self):
        return f"{self.first_name} - {self.course}"
