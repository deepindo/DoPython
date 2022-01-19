# Generated by Django 4.0 on 2022-01-19 07:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0002_alter_institution_alias_alter_institution_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='序号')),
                ('customer_name', models.CharField(max_length=20, verbose_name='客户姓名')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=5, verbose_name='性别')),
                ('customer_type', models.CharField(choices=[('医生', '医生'), ('药剂师', '药剂师'), ('KDM', 'KDM')], default='医生', max_length=10, verbose_name='客户类型')),
                ('customer_duty', models.CharField(choices=[('主任医师', '主任医师'), ('副主任医师', '副主任医师'), ('主治医师', '主治医师'), ('住院医师', '住院医师'), ('医生', '医生'), ('实习医生', '实习医生'), ('其他', '其他')], default='其他', max_length=10, verbose_name='客户职务')),
                ('customer_title', models.CharField(choices=[('院长', '院长'), ('副院长', '副院长'), ('主任', '主任'), ('副主任', '副主任'), ('组长', '组长'), ('副组长', '副组长'), ('其他', '其他')], default='其他', max_length=10, verbose_name='客户职称')),
                ('customer_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='客户电话')),
                ('approve_status', models.IntegerField(choices=[(1, '待审批'), (2, '审批通过'), (3, '审批拒绝')], default=1, verbose_name='审批状态')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('institution', models.ForeignKey(db_column='institution_id', on_delete=django.db.models.deletion.CASCADE, to='institution.institution')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'db_table': 'tb_customer',
            },
        ),
    ]
