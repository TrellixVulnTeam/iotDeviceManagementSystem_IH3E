# Generated by Django 3.2.5 on 2022-04-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iotapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='own_by_user',
            field=models.CharField(default='', max_length=200),
        ),
    ]