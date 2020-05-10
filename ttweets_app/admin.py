from django.contrib import admin
from . models import API_Credentials, App_Credentials

# Register your models here.
admin.site.register(API_Credentials)
admin.site.register(App_Credentials)

