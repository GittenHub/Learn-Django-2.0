# Generated by Django 2.0 on 2020-07-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200706_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
