# Generated by Django 3.0.4 on 2020-08-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previdenciarios', '0003_auto_20200827_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previdenciario',
            name='cpfPrev',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='previdenciario',
            name='whatsAppPrev',
            field=models.CharField(max_length=11),
        ),
    ]