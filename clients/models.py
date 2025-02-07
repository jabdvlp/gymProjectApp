from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100)
    second_surname = models.CharField(max_length=100, blank=True, null=True)

    DOC_ID_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjero'),
        ('PA', 'Pasaporte'),
    ]

    doc_id_type = models.CharField(max_length=2, choices=DOC_ID_CHOICES, default='Cédula de Ciudadanía')
    doc_id = models.CharField(max_length=20, unique=True, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    TRAINING_PLAN_CHOICES = [
        ('Musculacion', 'Musculacion'),
        ('Crossfit', 'Crossfit'),
        ('Full', 'Full'),
    ]

    training_plan = models.CharField(max_length=50, choices=TRAINING_PLAN_CHOICES, default='Musculacion')

