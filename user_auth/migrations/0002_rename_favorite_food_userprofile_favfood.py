# Generated by Django 5.0.4 on 2024-04-23 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favorite_food',
            new_name='favfood',
        ),
    ]
