# Generated by Django 4.1.1 on 2022-11-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eaddr',
            field=models.CharField(max_length=64),
        ),
    ]
