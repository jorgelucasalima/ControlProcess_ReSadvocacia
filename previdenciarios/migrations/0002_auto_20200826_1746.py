# Generated by Django 3.0.4 on 2020-08-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('previdenciarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previdenciario',
            name='beneficiosPrev',
            field=models.CharField(choices=[('Aposentadoria por Idade', 'Aposentadoria por Idade'), ('Aposentadoria por Tempo de Contribuição', 'Aposentadoria por Tempo de Contribuição'), ('Aposentadoria por Invalidez', 'Aposentadoria por Invalidez'), ('Pensão por Morte', 'Pensão por Morte'), ('Auxilio Doença', 'Auxilio Doença'), ('Auxilio Reclusão', 'Auxilio Reclusão'), ('Auxilio Maternidade', 'Auxilio Maternidade'), ('Benefícios Assistenciais', 'Benefícios Assistenciais'), ('Abono Anual', 'Abono Anual'), ('Revisão de Beneficio', 'Revisão de Beneficio'), ('Auxilio Acidente', 'Auxilio Acidente'), ('Acréscimo de 25/Porcentagem LOAS', 'Acréscimo de 25/Porcentagem LOAS')], max_length=100),
        ),
    ]
