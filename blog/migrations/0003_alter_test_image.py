# Generated by Django 5.0.7 on 2024-07-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(upload_to='testimage'),
        ),
    ]
