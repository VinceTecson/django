# Generated by Django 5.0.3 on 2024-04-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bajaj_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useracc',
            name='user_email',
        ),
        migrations.AddField(
            model_name='useracc',
            name='user_username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
