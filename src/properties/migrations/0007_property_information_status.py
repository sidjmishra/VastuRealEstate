# Generated by Django 3.0.2 on 2020-05-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20200527_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_information',
            name='status',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('Under-Construction', 'Under-Construction')], default='Rent', max_length=100),
        ),
    ]
