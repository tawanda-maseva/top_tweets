# Generated by Django 3.0.5 on 2020-05-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttweets_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=60)),
                ('api_secret_key', models.CharField(max_length=60)),
            ],
        ),
    ]