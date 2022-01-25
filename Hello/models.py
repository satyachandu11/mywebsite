from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Quotes(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    age = models.CharField(max_length=12)
    location = models.CharField(max_length=50)
    quot = models.TextField()
    date = models.DateField()    


    def __str__(self):
        return self.firstname