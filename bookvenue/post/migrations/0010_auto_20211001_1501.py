# Generated by Django 3.2.7 on 2021-10-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20211001_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
