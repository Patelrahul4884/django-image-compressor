# Generated by Django 3.1.2 on 2020-10-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('size_reducer', '0007_auto_20201013_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
