# Generated by Django 3.0.3 on 2020-09-05 05:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160312_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementaluser',
            name='username',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9-_]+$', message='Only alphanumeric characters are allowed.')]),
        ),
    ]
