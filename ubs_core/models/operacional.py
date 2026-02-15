from django.db import models
from .atendimento import *
from .registro import *


class Campanha(models.Model):
    id_campanha = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=100, blank=True, null=True)
    periodo_realizacao = models.CharField(max_length=100, blank=True, null=True)
    publico_alvo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campanha'
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'

    def __str__(self):
        return self.tema
        

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    qnt_estoque = models.IntegerField(blank=True, null=True)
    validade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamento'
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return self.nome

class Vacina(models.Model):
    id_vacina = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    faixa_etaria = models.CharField(max_length=50, blank=True, null=True)
    lote = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacina'
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'

    def __str__(self):
        return self.nome


class Prescricao(models.Model):
    id_prescricao = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey('Consulta', models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    data_retirada = models.DateField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescricao'
        verbose_name = 'Prescrição'
        verbose_name_plural = 'Prescrições'
