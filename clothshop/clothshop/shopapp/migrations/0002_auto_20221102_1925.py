# Generated by Django 3.2.12 on 2022-11-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prdtimage',
            name='images',
            field=models.FileField(upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank='True', upload_to='product'),
        ),
    ]
