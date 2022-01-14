# Generated by Django 4.0 on 2022-01-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('icon', models.ImageField(upload_to='icon/', verbose_name='人员头像')),
                ('name', models.CharField(max_length=15, verbose_name='人员姓名')),
                ('age', models.IntegerField(default=0, verbose_name='人员年龄')),
            ],
            options={
                'verbose_name': '人员管理',
                'verbose_name_plural': '人员管理',
                'db_table': 'dy_person',
            },
        ),
    ]
