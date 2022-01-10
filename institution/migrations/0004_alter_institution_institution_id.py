# Generated by Django 4.0 on 2022-01-10 08:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_alter_institution_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='institution_id',
            field=models.UUIDField(default=uuid.UUID('a2003251-41b9-49f4-a194-5efd5d345cfc'), editable=False, primary_key=True, serialize=False),
        ),
    ]
