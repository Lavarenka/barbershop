# Generated by Django 5.1.2 on 2024-10-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_socialitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='number',
            field=models.CharField(max_length=30, verbose_name='Number'),
        ),
    ]
