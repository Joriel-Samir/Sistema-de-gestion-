from django.forms import ModelForm
from .models import FinancialSummary

class FinancialForm(ModelForm): 
    class Meta:
        model = FinancialSummary
        fields = ("ingresos", "gastos", "fecha", "decripcion_gasto")

