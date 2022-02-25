# Generated by Django 4.0.2 on 2022-02-25 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_classaccesspackage_amount_of_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classaccesspackage',
            name='amount_of_tokens',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='classaccesspackage',
            name='duration',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(365)]),
        ),
    ]
