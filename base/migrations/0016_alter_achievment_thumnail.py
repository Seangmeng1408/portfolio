# Generated by Django 4.0.2 on 2022-02-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_achievment_thumnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievment',
            name='thumnail',
            field=models.ImageField(default='/default-thumbnail.jpg', null=True, upload_to='images'),
        ),
    ]
