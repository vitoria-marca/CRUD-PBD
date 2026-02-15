from django.db import models
from .operacional import *
from .registro import *

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    id_profissional = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_profissional', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

class Encaminhamento(models.Model):
    id_encaminhamento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    data_solicitacao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    agendado_por = models.ForeignKey('TecAdmin', models.DO_NOTHING, db_column='agendado_por', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encaminhamento'
        verbose_name = 'Encaminhamento'
        verbose_name_plural = 'Encaminhamentos'

    def __str__(self):
        return self.id_consulta.id_paciente.nome

class ParticipacaoCampanha(models.Model):
    id_paciente = models.OneToOneField(Paciente, models.DO_NOTHING, db_column='id_paciente', primary_key=True)
    id_campanha = models.ForeignKey('Campanha', models.DO_NOTHING, db_column='id_campanha')
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'participacao_campanha'
        unique_together = (('id_paciente', 'id_campanha', 'data'),)
        verbose_name = 'Participação em Campanha'
        verbose_name_plural = 'Participação em Campanhas'

class AplicacaoVacina(models.Model):
    id_paciente = models.OneToOneField('Paciente', models.DO_NOTHING, db_column='id_paciente', primary_key=True)
    id_vacina = models.ForeignKey('Vacina', models.DO_NOTHING, db_column='id_vacina')
    id_profissional = models.ForeignKey('Enfermeiro', models.DO_NOTHING, db_column='id_profissional', blank=True, null=True)
    data_aplicacao = models.DateField()
    dose = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacao_vacina'
        unique_together = (('id_paciente', 'id_vacina', 'data_aplicacao'),)
        verbose_name = 'Aplicação de Vacina'
        verbose_name_plural = 'Aplicação de Vacinas'
