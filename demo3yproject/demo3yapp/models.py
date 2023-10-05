from django.db import models


# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender_choices=(('male','Male'),('female','Female'),)
    gender=models.CharField(max_length=10,choices=gender_choices,null=True)
    email =models.CharField(max_length=100)
    phone =models.IntegerField(max_length=50)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    hobbies=models.CharField(max_length=50,blank=True)
    date_of_birth=models.DateField(null=True)
    DEPARTMENT_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
    ]

    COURSES_CHOICES = [
        ('Computer', 'Computer'),
        ('Biology', 'Biology'),
        ('BBA', 'BBA'),
        ('BCOM', 'BCOM'),
    ]

    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True)
    courses = models.CharField(max_length=50, choices=COURSES_CHOICES, blank=True)

    def str(self):
        return f'{self.department} - {self.courses}'
    def __str__(self):
        return self.first_name


