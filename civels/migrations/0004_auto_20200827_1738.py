# Generated by Django 3.0.4 on 2020-08-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civels', '0003_auto_20200827_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civel',
            name='protocoloCivel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='civel',
            name='whatsAppCivel',
            field=models.IntegerField(max_length=11),
        ),
    ]
