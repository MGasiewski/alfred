# Generated by Django 2.0.4 on 2018-04-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20180412_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]