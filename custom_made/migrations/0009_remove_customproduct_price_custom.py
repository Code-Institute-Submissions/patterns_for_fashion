# Generated by Django 3.1.4 on 2021-01-26 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_made', '0008_auto_20210120_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customproduct',
            name='price_custom',
        ),
    ]