# Generated by Django 3.0.6 on 2020-06-23 05:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0019_auto_20200623_0210'),

    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
