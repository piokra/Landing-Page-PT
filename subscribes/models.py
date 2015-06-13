from django.db import models

# Create your models here.

class Subscription(models.Model):
	ip = models.CharField(max_length=20)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return str(self.timestamp)+" "+self.email;


class Post(models.Model):
	author = models.CharField(max_length=20)
	title = models.CharField(max_length=20)
	hidden = models.BooleanField()
	short_content = models.CharField(max_length=120)
	full_content = models.CharField(max_length=4096)
	image = models.CharField(max_length=120)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return self.title