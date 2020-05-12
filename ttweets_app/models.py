from django.db import models

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

	class Meta:
		verbose_name_plural = 'User_access_tokens'






