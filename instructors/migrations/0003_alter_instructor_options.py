# Generated by Django 4.0.2 on 2022-03-09 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_alter_instructor_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['friendly_name']},
        ),
    ]
