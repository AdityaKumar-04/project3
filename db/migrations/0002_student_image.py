# Generated by Django 4.2.1 on 2023-11-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
