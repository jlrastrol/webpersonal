from django.db import models

# Create your models here.
class Project(models.Model):
    title =  models.CharField(max_length=200,verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha Creación")
    updated = models.DateTimeField(auto_now=True,verbose_name = "Fecha Actualización")

    class Meta:
        verbose_name = "projecto"
        verbose_name_plural = "projectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title