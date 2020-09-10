from django.db import models

# Create your models here.

class Previdenciario(models.Model):
    
    STATUS_BENEFICIOS = (
        ('Aposentadoria por Idade', 'Aposentadoria por Idade'),
        ('Aposentadoria por Tempo de Contribuição', 'Aposentadoria por Tempo de Contribuição'),
        ('Aposentadoria por Invalidez', 'Aposentadoria por Invalidez'),
        ('Pensão por Morte', 'Pensão por Morte'),
        ('Auxilio Doença', 'Auxilio Doença'),
        ('Auxilio Reclusão', 'Auxilio Reclusão'),
        ('Auxilio Maternidade', 'Auxilio Maternidade'),
        ('Benefícios Assistenciais', 'Benefícios Assistenciais'),
        ('Abono Anual', 'Abono Anual'),
        ('Revisão de Beneficio', 'Revisão de Beneficio'),
        ('Auxilio Acidente', 'Auxilio Acidente'),
        ('Acréscimo de 25/Porcentagem LOAS', 'Acréscimo de 25/Porcentagem LOAS'),

    )

    STATUS_ADV = (
        ('Dr. Itiel', 'Dr. Itiel'),
    )

    STATUS_DOC = (
        ('Pendente', 'Pendente'),
        ('Completo', 'Completo'),
    )


    nomePrev = models.CharField(max_length=255)
    cpfPrev = models.CharField(max_length=11)
    whatsAppPrev = models.CharField(max_length=11)
    beneficiosPrev = models.CharField(
        max_length=100,
        choices=STATUS_BENEFICIOS,
    )
    advogadoPrev = models.CharField(
        max_length=255,
        choices=STATUS_ADV,
    )
    protocoloPrev = models.CharField(max_length=100)
    statusDocPrev = models.CharField(
        max_length=100,
        choices=STATUS_DOC,
    )
    docPrev = models.FileField(upload_to='uploads/%Y/%m/%d/')
    criadoPrev = models.DateTimeField(auto_now_add=True)
    modificadoPrev = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomePrev