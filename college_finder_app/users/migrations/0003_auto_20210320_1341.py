# Generated by Django 3.1.4 on 2021-03-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='research',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, null=True),
        ),
    ]
