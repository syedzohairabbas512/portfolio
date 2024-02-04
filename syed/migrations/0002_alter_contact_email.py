# Generated by Django 3.2.12 on 2023-09-04 06:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')]),
        ),
    ]