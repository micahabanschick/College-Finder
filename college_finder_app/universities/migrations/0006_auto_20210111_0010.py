# Generated by Django 3.1.4 on 2021-01-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0005_auto_20210111_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universities',
            name='stats_female_male_ratio',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='universities',
            name='stats_number_students',
            field=models.CharField(max_length=16),
        ),
    ]