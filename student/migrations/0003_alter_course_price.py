# Generated by Django 4.1.5 on 2023-01-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
