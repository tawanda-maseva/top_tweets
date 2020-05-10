from django import forms
from . models import API_Credentials

class API_loginForm(forms.ModelForm):
    '''Form for collecting API login credentials'''
    class Meta:
    	model = API_Credentials
    	fields = ['api_key', 'api_secret_key', 'access_token', 'access_token_secret']
    	#labels  = {'api_key':'API Key', 'api_secret_key':'API Secret Key',
    	# 		'access_token':'Access Token', 'access_token_secret':'Access Token Secret'}
