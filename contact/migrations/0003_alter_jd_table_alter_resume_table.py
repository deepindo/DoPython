# Generated by Django 4.0 on 2021-12-29 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_jd_resume'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='jd',
            table='dy_JD',
        ),
        migrations.AlterModelTable(
            name='resume',
            table='dy_resume',
        ),
    ]
