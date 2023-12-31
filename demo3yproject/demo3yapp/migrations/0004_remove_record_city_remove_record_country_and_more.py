# Generated by Django 4.2.5 on 2023-10-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo3yapp', '0003_record_city_record_country_alter_record_hobbies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='city',
        ),
        migrations.RemoveField(
            model_name='record',
            name='country',
        ),
        migrations.AddField(
            model_name='record',
            name='courses',
            field=models.CharField(blank=True, choices=[('Computer', 'Computer'), ('Biology', 'Biology'), ('BBA', 'BBA'), ('BCOM', 'BCOM')], max_length=50),
        ),
        migrations.AddField(
            model_name='record',
            name='department',
            field=models.CharField(blank=True, choices=[('Science', 'Science'), ('Commerce', 'Commerce')], max_length=50),
        ),
    ]
