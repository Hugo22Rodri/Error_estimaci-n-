from django.db import models

class Estimacion(models.Model):
    muestras = models.IntegerField()
    error_estimacion = models.FloatField()
    nivel_confianza = models.FloatField()

    def __str__(self):
        return f"Estimación con {self.muestras} muestras"
