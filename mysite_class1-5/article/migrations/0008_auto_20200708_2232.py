# Generated by Django 2.0 on 2020-07-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]