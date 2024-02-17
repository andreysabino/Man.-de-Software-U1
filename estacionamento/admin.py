from django.contrib import admin
from estacionamento.models import Veiculo, Patio  # <--- import the model

# Register your models here.

admin.site.register(Veiculo)  # <--- register the model
admin.site.register(Patio) 