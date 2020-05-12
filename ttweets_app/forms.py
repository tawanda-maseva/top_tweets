from django import forms
from . models import Access_Tokens

class TokensForm(forms.ModelForm):
    '''Form for collecting API login credentials'''
    class Meta:
    	model = Access_Tokens
    	fields = ['access_token', 'access_token_secret']
    	labels  = {'access_token':'Access Token', 'access_token_secret':'Access Token Secret'}



class HashtagForm(forms.Form):
	'''Get #hashtag  input from user'''
	hashtag = forms.CharField(label='#Hashtag', max_length=50)

class SomeoneForm(forms.Form):
	'''Get #hashtag  input from user'''
	handle = forms.CharField(label='@handle', max_length=50)
    
