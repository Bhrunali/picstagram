# Generated by Django 3.0.6 on 2020-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0023_auto_20200627_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
