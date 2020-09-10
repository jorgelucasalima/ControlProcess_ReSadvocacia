from django.db import models

# Create your models here.

class Civel(models.Model):
    
    STATUS_BENEFICIOS = (
        ('Consumidor', 'Consumidor'),
        ('Familia', 'Familia'),
        ('Cobranças', 'Cobranças'),
        ('Responsabilidade Civil', 'Responsabilidade Civil'),

    )

    STATUS_TIPOS_BENEFICIOS = (
        ('Alimentos', 'Alimentos'),
        ('Divórcio', 'Divórcio'),
        ('Inventários', 'Inventários'),
        ('Investigação de paternidade', 'Investigação de paternidade'),
        ('Interdição', 'Interdição'),
        ('Recuperação de Créditos', 'Recuperação de Créditos'),
        ('Busca e Apreensão', 'Busca e Apreensão'),
        ('Revisional de Financiamentos', 'Revisional de Financiamentos'),
        ('Sem tipo', 'Sem tipo'),
    )

    STATUS_ADV = (
        ('Dr. Itiel', 'Dr. Itiel'),
    )

    STATUS_DOC = (
        ('Pendente', 'Pendente'),
        ('Completo', 'Completo'),
    )


    nomeCivel = models.CharField(max_length=255)
    cpfCivel = models.CharField(max_length=11)
    whatsAppCivel = models.CharField(max_length=11)
    beneficiosCivel = models.CharField(
        max_length=100,
        choices=STATUS_BENEFICIOS,
    )

    tiposBeneficiosCivel = models.CharField(
        max_length=100,
        choices=STATUS_TIPOS_BENEFICIOS,
        blank=True, null=True
    )

    advogadoCivel = models.CharField(
        max_length=255,
        choices=STATUS_ADV,
    )

    protocoloCivel = models.CharField(max_length=100)
    statusDocCivel = models.CharField(
        max_length=100,
        choices=STATUS_DOC,
    )
    docCivel = models.FileField(upload_to='uploads/%Y/%m/%d/')
    criadoCivel = models.DateTimeField(auto_now_add=True)
    modificadoCivel = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomeCivel