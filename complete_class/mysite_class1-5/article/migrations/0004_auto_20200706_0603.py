# Generated by Django 2.0 on 2020-07-06 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200706_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
