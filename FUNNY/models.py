from django.db import models


# Create your models here.

class UserDetailsModel(models.Model):
    firstName = models.CharField(max_length=30)

    lastName = models.CharField(max_length=30)

    emailId = models.EmailField(max_length=30)

    contactNo = models.CharField(max_length=10)

    streetAddress = models.TextField(max_length=30)

    city = models.CharField(max_length=30)

    state=models.CharField(max_length=20)

    country=models.CharField(max_length=30)

    zipCode = models.PositiveIntegerField(max_length=6)

    workStatus = models.CharField(max_length=10)

    education=models.CharField(max_length=30)

    skillSet = models.CharField(max_length=20)

    workExp=models.CharField(max_length=50)





