# Generated by Django 4.2.4 on 2023-08-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_tms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
