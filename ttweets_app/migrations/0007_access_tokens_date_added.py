# Generated by Django 3.0.5 on 2020-05-24 00:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ttweets_app', '0006_access_tokens_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='access_tokens',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]