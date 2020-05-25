from django.contrib import admin
from . models import App_Credentials, Access_Tokens, Profile_Tokens

# Register your models here.
admin.site.register(App_Credentials)
admin.site.register(Access_Tokens)
admin.site.register(Profile_Tokens)


