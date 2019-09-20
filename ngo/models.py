from django.db import models
from datetime import datetime

# Create your models here.
class NGO(models.Model):

	title = models.CharField(max_length=500)
	phone_number = models.CharField(max_length=100)
	description = models.TextField(blank = True)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	is_verified = models.BooleanField(default = False)
	post_date = models.DateTimeField(default = datetime.now(),blank = True)

	def __str__(self) : 
		return self.title

class Event(models.Model) : 
	
	title = models.CharField(max_length=500)
	ngo = 	models.ForeignKey(NGO,on_delete = models.CASCADE)
	location = models.CharField(max_length=200)
	description = models.TextField(blank = True)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	amount = models.IntegerField(default = 0)
	post_date = models.DateTimeField(default = datetime.now(),blank = True)

	def __str__(self) : 
		return self.title