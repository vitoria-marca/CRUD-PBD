from django.db import models

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
