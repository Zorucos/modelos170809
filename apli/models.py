from django.db import models
from django.core.urlresolvers import reverse


class Client(models.Model):
    nombre_completo = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    nickname = models.CharField(max_length=300)
    company_short = models.CharField(max_length=300)
    pais_address = models.CharField(max_length=50, blank=True, null=True)
    ciudad_address = models.CharField(max_length=100, blank=True, null=True)
    codigo_address = models.CharField(max_length=30, blank=True, null=True)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    numero_address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def get_absolute_url(self):
        return reverse('detail_contact', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre_completo


class Proyecto(models.Model):
    nombre = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    fecha_creacion = models.DateField()
    fecha_ejecucion = models.DateField()

    def get_absolute_url(self):
        return reverse('detail_project', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre_completo = models.CharField(max_length=300)
    nickname = models.CharField(max_length=300)
    adresse = models.CharField(max_length=300)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    sedcard = models.BooleanField(default=False)
    tipo = models.CharField(max_length=3, choices=(('mod', 'Modelo'), ('fot', 'Fotografo'), ('mak', 'Make Up'), ('sty', 'Styling'), ('rhh', 'Recursos Humanos'), ('otr', 'Styling')), default='mod')

    class Meta:
        verbose_name = 'Pesona'
        verbose_name_plural = 'Personas'

    def get_absolute_url(self):
        return reverse('detail_personas', kwargs={'pk': self.pk })

    def __str__(self):
        return self.nombre_completo


class Afectacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateField()
    inicio = models.TimeField()
    termino = models.TimeField()

    def __str__(self):
        return self.persona.nombre_completo + ' - ' + self.proyecto.nombre
