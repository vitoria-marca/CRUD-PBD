# ubs_core/admin/registros.py
from django.contrib import admin
from ..models import *

class AplicacaoVacinaInline(admin.TabularInline):
    model = AplicacaoVacina
    extra = 0 
    fields = ('id_vacina', 'id_profissional', 'data_aplicacao', 'dose')
    readonly_fields = ('data_aplicacao',) 
    can_delete = False

class ParticipacaoCampanhaInline(admin.TabularInline):
    model = ParticipacaoCampanha
    extra = 0
    fields = ('id_campanha', 'data')
    can_delete = False

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cartao_sus')
    search_fields = ('nome', 'cartao_sus')
    inlines = [AplicacaoVacinaInline, ParticipacaoCampanhaInline]

class MedicoInline(admin.StackedInline):
    model = Medico
    can_delete = False
    verbose_name_plural = 'Informações de Médico'
    fk_name = 'id_profissional'

class EnfermeiroInline(admin.StackedInline):
    model = Enfermeiro
    can_delete = False
    verbose_name_plural = 'Informações de Enfermeiro'
    fk_name = 'id_profissional'

class TecAdminInline(admin.StackedInline):
    model = TecAdmin
    can_delete = False
    verbose_name_plural = 'Informações de Técnico Administrativo'
    fk_name = 'id_profissional'

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    inlines = [MedicoInline, EnfermeiroInline, TecAdminInline]

    class Media:
        js = ('admin/js/toggle_inlines.js',)

    def get_inline_instances(self, request, obj=None):
        return [inline(self.model, self.admin_site) for inline in self.inlines]