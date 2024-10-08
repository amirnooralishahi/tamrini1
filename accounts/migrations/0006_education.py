# Generated by Django 5.0.7 on 2024-08-17 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('Degree', models.CharField(max_length=200)),
                ('field_of_study', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
