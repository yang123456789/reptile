from django.db import models


class ZhiLian(models.Model):
    position_name = models.CharField(max_length=50, null=False)
    company = models.CharField(max_length=100, null=False)
    salary = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=50, null=False)
    publish_date = models.CharField(max_length=20, null=False)
    requirements = models.TextField(null=False)

# Create your models here.
