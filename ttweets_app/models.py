from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone


# Create your models here.

class App_Credentials(models.Model):
	'''Keys to authenticate webapp with Tweeter API'''
	api_key = models.CharField(max_length=60)
	api_secret_key = models.CharField(max_length=60)

	class Meta:
		verbose_name_plural = 'App_Credentials'

	def __str__(self):
		'''Return string representation of model'''
		return 'Webapp Authentication'

class Access_Tokens(models.Model):
	'''User access tokens to their Tweeter accounts.'''

	# user app credentials
	api_key = models.CharField(max_length=60)
	api_secret_key = models.CharField(max_length=60)

	# user keys for accessing their tweeter
	access_token = models.CharField(max_length=60)
	access_token_secret = models.CharField(max_length=60)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

	class Meta:
		verbose_name_plural = 'User_access_tokens'


	def __str__(self):
		'''Return string representation of model'''
		return str(self.owner)

class Profile_Tokens(models.Model):
	'''Boolean for tracking is user has saved tokens to their profile'''
	saved_tokens = models.BooleanField(default=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'User_Profile_Tokens'

	def __str__(self):
		'''Return string representation of model'''
		return str(self.owner)








