# Generated by Django 4.2.4 on 2023-08-14 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager', '0004_password_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='key',
        ),
    ]