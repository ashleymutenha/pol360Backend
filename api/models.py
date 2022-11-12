from django.db import models
from  django.db.models  import JSONField


# Create your models here.

class Details(models.Model):
    details = JSONField()


class Brokers(models.Model):
    brokers =JSONField()
    status = models.CharField(max_length =200)


class Credentials(models.Model):
    username =  models.CharField(max_length =200)
    password =  models.CharField(max_length =200)


