# Generated by Django 3.0.6 on 2020-06-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0016_auto_20200622_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
