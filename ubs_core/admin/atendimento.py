from django.contrib import admin
from ..models.atendimento import *

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data', 'horario', 'id_paciente', 'id_profissional')
    list_select_related = ('id_profissional__id_profissional', 'id_paciente')
    search_fields = ('id_profissional', 'id_paciente', 'data',)

    def nome_medico(self, obj):
        return obj.id_profissional.nome
    nome_medico.short_description = 'Médico'

@admin.register(Encaminhamento)
class EncaminhamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'data_solicitacao', 'status', 'agendado_por', 'get_paciente')
    list_select_related = ('id_consulta__id_paciente', 'agendado_por__id_profissional')
    list_filter = ('status', 'tipo')
    search_fields = ('status', 'id_consulta__id_paciente__nome', 'tipo')

    def get_paciente(self, obj):
        return obj.id_consulta.id_paciente.nome if obj.id_consulta else "N/A"
    get_paciente.short_description = 'Paciente'

@admin.register(ParticipacaoCampanha)
class ParticipacaoCampanhaAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'id_campanha', 'data')
    list_select_related = ('id_paciente', 'id_campanha')
    list_filter = ('data', 'id_campanha')
    search_fields = ('id_paciente__nome', 'id_campanha__tema')

@admin.register(AplicacaoVacina)
class AplicacaoVacinaAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'id_vacina', 'dose', 'data_aplicacao', 'id_profissional')
    list_select_related = ('id_paciente', 'id_vacina', 'id_profissional__id_profissional')
    list_filter = ('data_aplicacao', 'dose', 'id_vacina')
    search_fields = ('id_paciente__nome', 'id_vacina__nome')