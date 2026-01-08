from django.db import models
from django.utils import timezone

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Lead(models.Model):
    ESTADO_CHOICES = [
        ('NUEVO', 'Nuevo'),
        ('CONTACTADO', 'Contactado'),
        ('INTERESADO', 'Interesado'),
        ('POSTULANTE', 'En Proceso de Admisión'),
        ('MATRICULADO', 'Matriculado'),
        ('PERDIDO', 'Perdido/No Interesado'),
    ]

    ORIGEN_CHOICES = [
        ('FACEBOOK', 'Facebook Ads'),
        ('INSTAGRAM', 'Instagram'),
        ('TIKTOK', 'TikTok'),
        ('WEB', 'Pagina Web'),
        ('REFERIDO', 'Referido'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    colegio = models.CharField(max_length=100)
    dir_colegio = models.CharField(max_length=100)
    
    
    carrera_interes = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, related_name='aspirantes')
    origen = models.CharField(max_length=20, choices=ORIGEN_CHOICES, default='WEB')
    
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='NUEVO')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.estado}"

class Interaccion(models.Model):
    TIPO_CHOICES = [
        ('LLAMADA', 'Llamada Telefónica'),
        ('WHATSAPP', 'Mensaje de WhatsApp'),
        ('EMAIL', 'Correo Electrónico'),
        ('REUNION', 'Reunión Presencial'),
    ]

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='interacciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    notas = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo} con {self.lead.nombre} - {self.fecha.strftime('%d/%m/%Y')}"