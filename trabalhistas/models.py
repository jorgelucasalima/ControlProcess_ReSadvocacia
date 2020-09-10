from django.db import models

# Create your models here.

class Trabalhista(models.Model):
    
    STATUS_BENEFICIOS = (
        ('Trabalhista', 'Trabalhista'),
    )

    STATUS_ADV = (
        ('Dr. Itiel', 'Dr. Itiel'),
    )

    STATUS_DOC = (
        ('Pendente', 'Pendente'),
        ('Completo', 'Completo'),
    )


    nomeTrab = models.CharField(max_length=255)
    cpfTrab = models.CharField(max_length=11)
    whatsAppTrab = models.CharField(max_length=11)
    beneficiosTrab = models.CharField(
        max_length=100,
        choices=STATUS_BENEFICIOS,
    )
    advogadoTrab = models.CharField(
        max_length=255,
        choices=STATUS_ADV,
    )
    protocoloTrab = models.CharField(max_length=100)
    statusDocTrab = models.CharField(
        max_length=100,
        choices=STATUS_DOC,
    )
    docTrab = models.FileField(upload_to='uploads/%Y/%m/%d/')
    criadoTrab = models.DateTimeField(auto_now_add=True)
    modificadoTrab = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomeTrab


   