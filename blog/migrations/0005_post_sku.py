# Generated by Django 3.1.4 on 2021-02-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210211_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
