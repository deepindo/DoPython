# Generated by Django 4.0 on 2021-12-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_award_photo_alter_award_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='图片描述'),
        ),
        migrations.AlterField(
            model_name='award',
            name='photo',
            field=models.ImageField(blank=True, upload_to='award/', verbose_name='图片地址'),
        ),
    ]