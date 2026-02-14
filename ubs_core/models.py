from django.db import models

class Campanha(models.Model):
    id_campanha = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=100, blank=True, null=True)
    periodo_realizacao = models.CharField(max_length=100, blank=True, null=True)
    publico_alvo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campanha'
        
class Profissional(models.Model):
    id_profissional = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profissional'

class Medico(models.Model):
    id_profissional = models.OneToOneField('Profissional', models.DO_NOTHING, db_column='id_profissional', primary_key=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    crm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'

class Enfermeiro(models.Model):
    id_profissional = models.OneToOneField('Profissional', models.DO_NOTHING, db_column='id_profissional', primary_key=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    coren = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermeiro'

class TecAdmin(models.Model):
    id_profissional = models.OneToOneField(Profissional, models.DO_NOTHING, db_column='id_profissional', primary_key=True)

    class Meta:
        managed = False
        db_table = 'tec_admin'

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    cartao_sus = models.CharField(max_length=20, blank=True, null=True)
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'

class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    qnt_estoque = models.IntegerField(blank=True, null=True)
    validade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamento'

class Vacina(models.Model):
    id_vacina = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    faixa_etaria = models.CharField(max_length=50, blank=True, null=True)
    lote = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacina'

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

class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente', blank=True, null=True)
    id_profissional = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_profissional', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'

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

class ParticipacaoCampanha(models.Model):
    id_paciente = models.OneToOneField(Paciente, models.DO_NOTHING, db_column='id_paciente', primary_key=True)
    id_campanha = models.ForeignKey(Campanha, models.DO_NOTHING, db_column='id_campanha')
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'participacao_campanha'
        unique_together = (('id_paciente', 'id_campanha', 'data'),)

class Prescricao(models.Model):
    id_prescricao = models.AutoField(primary_key=True)
    id_consulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='id_consulta', blank=True, null=True)
    id_medicamento = models.ForeignKey(Medicamento, models.DO_NOTHING, db_column='id_medicamento', blank=True, null=True)
    data_retirada = models.DateField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescricao'
