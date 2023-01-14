# Generated by Django 4.1.5 on 2023-01-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname_patient', models.CharField(max_length=64)),
                ('lastname_patient', models.CharField(max_length=64)),
                ('birthdate_patient', models.DateField()),
                ('admittingtime_patient', models.DateTimeField()),
                ('dischargetime_patien', models.DateTimeField(blank=True, default='', null=True)),
            ],
        ),
    ]