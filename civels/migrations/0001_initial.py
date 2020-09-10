# Generated by Django 3.0.4 on 2020-08-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Civel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCivel', models.CharField(max_length=255)),
                ('cpfCivel', models.CharField(max_length=11)),
                ('whatsAppCivel', models.CharField(max_length=9)),
                ('beneficiosCivel', models.CharField(choices=[('Aposentadoria por Idade', 'Aposentadoria por Idade'), ('Aposentadoria por Tempo de Contribuição', 'Aposentadoria por Tempo de Contribuição'), ('Aposentadoria por Invalidez', 'Aposentadoria por Invalidez'), ('Pensão por Morte', 'Pensão por Morte'), ('Auxilio Doença', 'Auxilio Doença'), ('Auxilio Reclusão', 'Auxilio Reclusão'), ('Auxilio Maternidade', 'Auxilio Maternidade'), ('Benefícios Assistenciais', 'Benefícios Assistenciais'), ('Abono Anual', 'Abono Anual'), ('Revisão de Beneficio', 'Revisão de Beneficio'), ('Auxilio Acidente', 'Auxilio Acidente')], max_length=100)),
                ('tiposBeneficiosCivel', models.CharField(choices=[('Alimentos', 'Alimentos'), ('Divórcio', 'Divórcio'), ('Inventários', 'Inventários'), ('Investigação de paternidade', 'Investigação de paternidade'), ('Interdição', 'Interdição'), ('Recuperação de Créditos', 'Recuperação de Créditos'), ('Busca e Apreensão', 'Busca e Apreensão'), ('Revisional de Financiamentos', 'Revisional de Financiamentos'), ('Sem tipo', 'Sem tipo')], max_length=100)),
                ('advogadoCivel', models.CharField(choices=[('Dr. Itiel', 'Dr. Itiel')], max_length=255)),
                ('protocoloCivel', models.CharField(max_length=255)),
                ('statusDocCivel', models.CharField(choices=[('Pendente', 'Pendente'), ('Completo', 'Completo')], max_length=100)),
                ('docCivel', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('criadoCivel', models.DateTimeField(auto_now_add=True)),
                ('modificadoCivel', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
