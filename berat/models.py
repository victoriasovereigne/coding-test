from django.db import models
from datetime import datetime

# Create your models here.
class Berat(models.Model):
	tanggal = models.DateTimeField('Tanggal', default=datetime.now())
	berat_max = models.IntegerField(default=0)
	berat_min = models.IntegerField(default=0)
	diff = models.IntegerField(default=0)