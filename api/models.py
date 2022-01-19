from django.db import models

# Create your models here.
class Airplane(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	passenger = models.PositiveIntegerField()


