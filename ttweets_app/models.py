from django.db import models

# Create your models here.
class API_Credentials(models.Model):
	'''Captures user credentials to use Tweeter API'''

	# keys for searching on tweeter
	api_key = models.CharField(max_length=60)
	api_secret_key = models.CharField(max_length=60)

	# Keys for searching from user timeline
	access_token = models.CharField(max_length=60)
	access_token_secret = models.CharField(max_length=60)
