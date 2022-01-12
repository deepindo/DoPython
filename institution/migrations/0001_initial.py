# Generated by Django 4.0 on 2022-01-12 08:12

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('institution_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('serial_number', models.IntegerField(default=1, verbose_name='序号')),
                ('institution_code', models.CharField(max_length=20, verbose_name='机构编码')),
                ('name', models.CharField(max_length=10, verbose_name='机构名称')),
                ('alias', models.CharField(blank=True, max_length=30, null=True, verbose_name='机构别名')),
                ('province', models.CharField(max_length=20, verbose_name='省份')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('area', models.CharField(blank=True, max_length=20, null=True, verbose_name='区县')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='详细地址')),
                ('institution_type', models.CharField(choices=[('专科医院', '专科医院'), ('综合医院', '综合医院'), ('单体药店', '单体药店'), ('连锁药店门店', '连锁药店门店'), ('连锁药店总店', '连锁药店总店'), ('诊所', '诊所'), ('其他', '其他')], max_length=100, verbose_name='机构类别')),
                ('institution_property', models.IntegerField(choices=[(1, '民营医院'), (2, '公立医院'), (3, '专科医院'), (4, '未知')], verbose_name='机构性质')),
                ('institution_character', models.IntegerField(choices=[(1, 'Common'), (2, 'COE'), (3, 'Focus')], default=1, verbose_name='机构属性')),
                ('post_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='邮政编码')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='机构电话')),
                ('approve_status', models.IntegerField(choices=[(1, '待审批'), (2, '审批通过'), (3, '审批拒绝')], default=1, verbose_name='审批状态')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机构信息',
                'verbose_name_plural': '机构信息',
                'db_table': 'dy_institution',
            },
        ),
    ]
