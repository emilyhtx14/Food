# Generated by Django 3.1.5 on 2021-01-16 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='user',
        ),
    ]