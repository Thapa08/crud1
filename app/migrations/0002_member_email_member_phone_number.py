# Generated by Django 4.2.1 on 2023-05-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
