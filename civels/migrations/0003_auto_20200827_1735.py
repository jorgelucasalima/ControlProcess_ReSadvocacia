# Generated by Django 3.0.4 on 2020-08-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civels', '0002_auto_20200826_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civel',
            name='cpfCivel',
            field=models.IntegerField(max_length=11),
        ),
        migrations.AlterField(
            model_name='civel',
            name='whatsAppCivel',
            field=models.IntegerField(max_length=9),
        ),
    ]
