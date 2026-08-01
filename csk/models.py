from django.db import models
# Create your models here.

class players (models.Model):
	name = models.CharField(max_length = 20)
	age = models.IntegerField()
	
	def __str__(self):
		return f"Name: {self.name} age: {self.age} "