from django.contrib import admin
from ..models.operacional import *

@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('tema', 'periodo_realizacao', 'publico_alvo')
    search_fields = ('tema',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fabricante', 'qnt_estoque', 'validade')
    list_filter = ('fabricante', 'validade')
    search_fields = ('nome',)

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fabricante', 'lote', 'faixa_etaria')
    search_fields = ('nome', 'lote')

@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ('id_prescricao', 'id_consulta', 'id_medicamento', 'data_retirada', 'quantidade')
    list_filter = ('data_retirada',)
    autocomplete_fields = ('id_medicamento',)