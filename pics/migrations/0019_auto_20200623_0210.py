# Generated by Django 3.0.6 on 2020-06-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0018_auto_20200623_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
