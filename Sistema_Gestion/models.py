from django.db import models
from django.conf import settings

class FinancialSummary(models.Model):
    ingresos = models.DecimalField(max_digits=12, decimal_places=2)
    gastos = models.DecimalField(max_digits=12, decimal_places=2)
    decripcion_gasto = models.TextField(blank=True,max_length=200)
    fecha = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"by {self.user.username}"