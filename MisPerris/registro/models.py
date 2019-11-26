from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

ESTADO_CHOICES = [
    ('RS', 'Rescatado'),
    ('DS', 'Disponible'),
    ('AD', 'Adoptado'),
]

REGION_CHOICES = [
    ('', 'Seleccionar'),
    ('RM', 'Region Metropolitana'),
    ('AP', 'Arica y Parinacota'),
    ('TA', 'Tarapacá'),
    ('AN', 'Antofagasta'),
    ('AT', 'Atacama'),
    ('CO', 'Coquimbo'),
    ('VA', 'Valparaiso'),
    ('OH', "O'higgins"),
    ('MA', 'Maule'),
    ('NB', 'Ñuble'),
    ('BI', 'Biobío'),
    ('AR', 'La Araucanía'),
    ('LR', 'Los Ríos'),
    ('LL', 'Los Lagos'),
    ('AI', 'Aysén'),
    ('MG', 'Magallanes'),
]

CIUDAD_CHOICES = [
    ('', 'Seleccionar'),
    ('AN', 'Antofagasta'),
    ('AR', 'Arica'),
    ('BU', 'Buin'),
    ('CA', 'Calama'),
    ('CH', 'Chillán'),
    ('CO', 'Colina'),
    ('CC', 'Concepción'),
    ('CP', 'Copiapó'),
    ('CY', 'Coyhaique'),
    ('CU', 'Curicó'),
    ('IQ', 'Iquique'),
    ('LS', 'La Serena'),
    ('LI', 'Limache'),
    ('LN', 'Linares'),
    ('LA', 'Los Andes'),
    ('LG', 'Los Ángeles'),
    ('ME', 'Melipilla'),
    ('OS', 'Osorno'),
    ('OV', 'Ovalle'),
    ('PE', 'Peñaflor'),
    ('PM', 'Puerto Montt'),
    ('PA', 'Punta Arenas'),
    ('QU', 'Quillota'),
    ('RA', 'Rancagua'),
    ('ST', 'Santiago'),
    ('SA', 'San Antonio'),
    ('SB', 'San Bernardo'),
    ('SF', 'San Felipe'),
    ('TA', 'Talagante'),
    ('TC', 'Talca'),
    ('TE', 'Temuco'),
    ('VA', 'Valdivia'),
    ('VP', 'Valparaíso'),
]

VIVIENDA_CHOICES = [
    ('', 'Seleccionar'),
    ('CS1', 'Casa con patio grande'),
    ('CS2', 'Casa con patio pequeño'),
    ('CS3', 'Casa sin patio'),
    ('DTO', 'Departamento'),
]

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, default='voluntario')
    rut = models.CharField(max_length=12, default='12345678-9')
    fechanacimiento = models.DateField(default=timezone.now)
    telefono = models.PositiveIntegerField(default=0)
    region = models.CharField(
        default='RM',
        max_length=50,
        choices=REGION_CHOICES,
    )
    ciudad = models.CharField(
        default='ST',
        max_length=50,
        choices=CIUDAD_CHOICES,
    )
    tipovivienda = models.CharField(
        default='CS3',
        max_length=50,
        choices=VIVIENDA_CHOICES,
    )
    
    def __str__(self):
        return self.usuario.username

#class Rescatado(models.Model):
#    autor = models.OneToOneField(User, on_delete=models.CASCADE)
#    imagen = models.ImageField(upload_to=settings.IMAGE_UPLOAD , default='/static/None/no-img.jpg')
#    nombre = models.CharField(max_length=50)
#    raza = models.CharField(max_length=50)
#    descripcion = models.CharField(max_length=200)
#    estado = models.CharField(
#        max_length=50,
#        choices=ESTADO_CHOICES,
#    )
#
#    def __autor__(self):
#        return self.autor.username
#
#    def __str__(self):
#        return self.nombre