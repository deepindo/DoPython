# Generated by Django 4.0 on 2022-01-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ID_number',
            field=models.CharField(max_length=18, verbose_name='身份证号'),
        ),
    ]
