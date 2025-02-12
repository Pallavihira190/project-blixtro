from django.db import models

# Create your models here.
class Organisation(models.Model):
    organisation_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)


class Department(models.Model):
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    udpated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)



