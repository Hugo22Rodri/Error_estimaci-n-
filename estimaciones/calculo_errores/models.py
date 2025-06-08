from django.db import models
from django.conf import settings

class CalculoErrores(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    valor_real = models.FloatField()
    valor_aprox = models.FloatField()
    error_abs = models.FloatField()
    error_rel = models.FloatField()
    error_porc = models.FloatField()
    fecha_calculo = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cálculo del {self.fecha_calculo.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Cálculo de Errores"
        verbose_name_plural = "Cálculos de Errores"
        ordering = ['-fecha_calculo']