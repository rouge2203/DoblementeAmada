# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientas(models.Model):
    idclienta = models.AutoField(db_column='idClienta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    celular = models.CharField(max_length=45, blank=True, null=True)
    instagram = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=45, blank=True, null=True)
    canton = models.CharField(max_length=45, blank=True, null=True)
    distrito = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    envio = models.CharField(max_length=45, blank=True, null=True)
    porcentaje_ganancia = models.IntegerField(blank=True, null=True)
    metodo_pago = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientas'
