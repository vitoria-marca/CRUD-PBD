from django.db import models


class Profissional(models.Model):
 
    class Tipo(models.TextChoices):
        TECADMIN = 'Tec Administrativo'
        MEDICO = 'Medico' 
        ENFERMEIRO = 'Enfermeiro'
    
    id_profissional = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    carga_horaria = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(choices=Tipo.choices, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profissional'
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'    

class Medico(models.Model):
    id_profissional = models.OneToOneField('Profissional', models.DO_NOTHING, db_column='id_profissional', primary_key=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    crm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return self.id_profissional.nome
    

class Enfermeiro(models.Model):
    id_profissional = models.OneToOneField('Profissional', models.DO_NOTHING, db_column='id_profissional', primary_key=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    coren = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermeiro'
        verbose_name = 'Enfermeiro'
        verbose_name_plural = 'Enfermeiros'

class TecAdmin(models.Model):
    id_profissional = models.OneToOneField(Profissional, models.DO_NOTHING, db_column='id_profissional', primary_key=True)

    class Meta:
        managed = False
        db_table = 'tec_admin'
        verbose_name = 'Técnico Administrativo'
        verbose_name_plural = 'Técnicos Administrativos'

class Paciente(models.Model):

    class Sexo(models.TextChoices):
        FEMININO = 'F','FEMININO'
        MASCULINO ='M', 'MASCULINO' 
        NAOBINARIO ='N', 'NÃO BINÁRIO'

    id_paciente = models.AutoField(primary_key=True)
    cartao_sus = models.CharField(max_length=20, blank=False, null=False)
    nome = models.CharField(max_length=100, null=False)
    data_nasc = models.DateField(blank=True, null=True)
    sexo = models.CharField(choices=Sexo.choices,max_length=1, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pecientes'

    def __str__(self):
        return self.nome
