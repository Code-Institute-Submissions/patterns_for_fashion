# Generated by Django 3.1.4 on 2021-02-11 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='sku',
        ),
    ]
