# Generated by Django 4.0 on 2021-12-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_about_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='work',
            field=models.CharField(default='Programmer', max_length=30),
        ),
    ]