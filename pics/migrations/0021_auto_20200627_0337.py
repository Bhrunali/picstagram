# Generated by Django 3.0.6 on 2020-06-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0020_auto_20200623_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='ProfilePciture/'),
        ),
    ]