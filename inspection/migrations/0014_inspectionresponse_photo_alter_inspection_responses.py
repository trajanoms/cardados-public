# Generated by Django 4.2 on 2024-06-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0013_remove_inspectionresponse_inspection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspectionresponse',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Foto do item'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='responses',
            field=models.ManyToManyField(related_name='inspection', to='inspection.inspectionresponse'),
        ),
    ]
