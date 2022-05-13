# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from pydoc import classname
from pyexpat import model
from re import T
from django.db import models










class Puntos(models.Model):
    paciente  = models.BigIntegerField(null=True, blank=True)
    Puntos  = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.paciente



class Acceso(models.Model):
    usuarioid = models.IntegerField(primary_key=True)
    opcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'acceso'
        unique_together = (('usuarioid', 'opcion'),)


class Activo(models.Model):
    activoid = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_asignacion = models.DateTimeField(blank=True, null=True)
    categoriaid = models.IntegerField()
    proveedorid = models.IntegerField(blank=True, null=True)
    tipoproductoid = models.IntegerField(blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    costo_compra = models.DecimalField(max_digits=18, decimal_places=2)
    fecha_compra = models.DateTimeField(blank=True, null=True)
    factura_compra = models.CharField(max_length=50, blank=True, null=True)
    forma_adquisicion = models.CharField(max_length=1)
    costo_original = models.DecimalField(max_digits=18, decimal_places=2)
    itbis = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=3)
    porciento_limite = models.DecimalField(max_digits=10, decimal_places=2)
    no_archivo = models.CharField(max_length=10, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)
    vendido = models.IntegerField()
    vida_util = models.IntegerField()
    valor_residual = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_depreciacion = models.CharField(max_length=1)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    depreciar = models.IntegerField()
    fecha_limite = models.DateTimeField(blank=True, null=True)
    mantenimiento = models.IntegerField()
    proximo_mantenimiento = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activo'


class ActivoMantenimiento(models.Model):
    mantenimientoid = models.AutoField(primary_key=True)
    activoid = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    tipomantenimientoid = models.IntegerField()
    exterior = models.IntegerField()
    fecha_salida = models.DateTimeField(blank=True, null=True)
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    proxima_fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    proveedorid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activo_mantenimiento'


class ActivoMovimiento(models.Model):
    movimientoid = models.AutoField(primary_key=True)
    activoid = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=1)
    concepto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activo_movimiento'


class Admision(models.Model):
    admisionid = models.AutoField(primary_key=True)
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    habitacionid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    tipoadmisionid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    camaid = models.IntegerField(blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    resp_nombre = models.CharField(max_length=80, blank=True, null=True)
    resp_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    resp_telefono = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    parentescoid = models.IntegerField(blank=True, null=True)
    hospitalizacion = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    autorizacionid = models.IntegerField(blank=True, null=True)
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    resp_identificacion = models.CharField(max_length=20, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    resp_cedula = models.CharField(max_length=20, blank=True, null=True)
    certificadoid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    entregada = models.IntegerField(blank=True, null=True)
    usuarioid_entregada = models.IntegerField(blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    cobertura_disponible = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid_cobertura_disponible = models.CharField(max_length=100, blank=True, null=True)
    hora_ultima_medicacion = models.DateTimeField(blank=True, null=True)
    habitacion_numero = models.CharField(max_length=15, blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    descuento_servicio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    triaje_nivel = models.CharField(max_length=20, blank=True, null=True)
    hora_factura = models.DateTimeField(blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    usuarioid_reversa = models.IntegerField(blank=True, null=True)
    fecha_reversa = models.DateTimeField(blank=True, null=True)
    auditoria_nota_medica = models.CharField(max_length=2000, blank=True, null=True)
    honorarioid = models.IntegerField(blank=True, null=True)
    estatusid = models.IntegerField(blank=True, null=True)
    auditorid_administrativo = models.IntegerField(blank=True, null=True)
    auditorid_medico = models.IntegerField(blank=True, null=True)
    tipoglosaid = models.IntegerField(blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota_concurrencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    detalle_incidencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipoincidenciaid = models.IntegerField(blank=True, null=True)
    fecha_recibe_seguro = models.DateTimeField(blank=True, null=True)
    fecha_entrega_auditor = models.DateTimeField(blank=True, null=True)
    fecha_recepcion_auditor = models.DateTimeField(blank=True, null=True)
    auditoria_glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    auditoria_observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_entrega_seguro = models.DateTimeField(blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    facturaintid = models.IntegerField(blank=True, null=True)
    resp_parentesco = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision'


class AdmisionAlta(models.Model):
    altaid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    salida_donde = models.CharField(max_length=1, blank=True, null=True)
    salida_condicion = models.CharField(max_length=1, blank=True, null=True)
    dias_incapacidad = models.IntegerField(blank=True, null=True)
    muerto = models.IntegerField(blank=True, null=True)
    causa_muerte = models.CharField(max_length=200, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_alta'


class AdmisionAuditoria(models.Model):
    notaid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    leida = models.IntegerField(blank=True, null=True)
    usuarioid_lee = models.IntegerField(blank=True, null=True)
    fecha_lee = models.DateTimeField(blank=True, null=True)
    hora_lee = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_auditoria'


class AdmisionAuditoriaMedica(models.Model):
    auditoriaid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admision_auditoria_medica'


class AdmisionAuditoriaMedicaDetalle(models.Model):
    auditoriaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    conceptoid = models.IntegerField(blank=True, null=True)
    valor = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_auditoria_medica_detalle'
        unique_together = (('auditoriaid', 'detalleid'),)


class AdmisionCalendario(models.Model):
    calendarioid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    signos = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    productoid = models.IntegerField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_calendario'


class AdmisionDieta(models.Model):
    admisionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    dietaid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    desayuno_hora = models.DateTimeField(blank=True, null=True)
    desayuno_texto = models.TextField(blank=True, null=True)  # This field type is a guess.
    comida_hora = models.DateTimeField(blank=True, null=True)
    comida_texto = models.TextField(blank=True, null=True)  # This field type is a guess.
    cena_hora = models.DateTimeField(blank=True, null=True)
    cena_texto = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admision_dieta'
        unique_together = (('admisionid', 'detalleid'),)


class AdmisionEstudio(models.Model):
    admisionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codigo_seguro = models.CharField(max_length=6, blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    enviado_laboratorio = models.IntegerField(blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    laboratorioid = models.IntegerField(blank=True, null=True)
    usuarioid_inserta = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    fecha_inserta = models.DateTimeField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid_elimina = models.IntegerField(blank=True, null=True)
    fecha_elimina = models.DateTimeField(blank=True, null=True)
    quirurgico = models.CharField(max_length=1, blank=True, null=True)
    exclusion_internacional = models.IntegerField()
    uci = models.IntegerField()
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    simon = models.CharField(max_length=10, blank=True, null=True)
    validar_informe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admision_estudio'
        unique_together = (('admisionid', 'detalleid'),)


class AdmisionHonorario(models.Model):
    admisionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobrar = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_honorario'
        unique_together = (('admisionid', 'detalleid'),)


class AdmisionHonorarioManual(models.Model):
    admisionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_honorario_manual'
        unique_together = (('admisionid', 'detalleid'),)


class AdmisionInforme(models.Model):
    informeid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admision_informe'


class AdmisionInterconsulta(models.Model):
    interconsultaid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    hallazgos = models.TextField(blank=True, null=True)  # This field type is a guess.
    recomendacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    diagnostico = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admision_interconsulta'


class AdmisionLog(models.Model):
    logid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_log'


class AdmisionMedicacion(models.Model):
    medicacionid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    productoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()
    nota_medica = models.TextField(blank=True, null=True)  # This field type is a guess.
    nota_enfermera = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admision_medicacion'


class AdmisionNacido(models.Model):
    nacidoid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    vivo = models.CharField(max_length=1, blank=True, null=True)
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_fallecido = models.DateTimeField(blank=True, null=True)
    apellido = models.CharField(max_length=80, blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    hora_nacido = models.DateTimeField(blank=True, null=True)
    hora_fallecido = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admision_nacido'


class AdmisionProcedimiento(models.Model):
    procedimientoid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField()
    cie10 = models.CharField(max_length=10)
    quirurgico_descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid_cirujano = models.IntegerField(blank=True, null=True)
    medicoid_anestesia = models.IntegerField(blank=True, null=True)
    medicoid_ayudante = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admision_procedimiento'


class AdmisionResumen(models.Model):
    admisionid = models.IntegerField(primary_key=True)
    servicioid = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porciento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rechazado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admision_resumen'
        unique_together = (('admisionid', 'servicioid'),)


class AdmisionSignosVitales(models.Model):
    signosid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    ta = models.CharField(max_length=15, blank=True, null=True)
    fc = models.CharField(max_length=15, blank=True, null=True)
    pulso = models.CharField(max_length=15, blank=True, null=True)
    temperatura = models.CharField(max_length=15, blank=True, null=True)
    fr = models.CharField(max_length=15, blank=True, null=True)
    diuresis = models.CharField(max_length=15, blank=True, null=True)
    estado_vigilia = models.CharField(max_length=20, blank=True, null=True)
    morse = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    so = models.CharField(max_length=15, blank=True, null=True)
    glicemia = models.CharField(max_length=20, blank=True, null=True)
    downton = models.CharField(max_length=30, blank=True, null=True)
    evolucionid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admision_signos_vitales'


class Almacen(models.Model):
    almacenid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    negativo = models.CharField(max_length=1, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacen'


class Anexo(models.Model):
    anexoid = models.AutoField(primary_key=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anexo'


class AnexoDetalle(models.Model):
    anexoid = models.IntegerField(primary_key=True)
    cuentaid = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'anexo_detalle'
        unique_together = (('anexoid', 'cuentaid'),)


class AnoFiscal(models.Model):
    ano = models.IntegerField(primary_key=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ano_fiscal'


class Auditoria(models.Model):
    auditoriaid = models.AutoField(primary_key=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    farmacia = models.IntegerField(blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'auditoria'


class AuditoriaDetalle(models.Model):
    auditoriaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=3)
    servicioid = models.IntegerField()
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    usuarioid_cierre = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    auditadas = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nota = models.CharField(max_length=1, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    facturada = models.IntegerField(blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'auditoria_detalle'
        unique_together = (('auditoriaid', 'detalleid', 'tipo', 'servicioid'),)


class AuditoriaMedicaEstatus(models.Model):
    estatusid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_medica_estatus'


class AutorizacionAlta(models.Model):
    autorizacionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    dias_incapacidad = models.IntegerField(blank=True, null=True)
    aconseja = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'autorizacion_alta'


class AutorizacionPalic(models.Model):
    autorizacionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    diagnostico = models.CharField(max_length=5, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorizacion_palic'


class AutorizacionUniversal(models.Model):
    autorizacionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    diagnostico = models.CharField(max_length=5, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autorizacion_universal'


class Banco(models.Model):
    bancoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    rnc = models.CharField(max_length=30, blank=True, null=True)
    banco_codigo = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco'


class BancoConciliacion(models.Model):
    conciliacionid = models.AutoField(primary_key=True)
    bancocuentaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    balance_banco = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_conciliacion'


class BancoConciliacionTransito(models.Model):
    conciliacionid = models.IntegerField(primary_key=True)
    transaccionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banco_conciliacion_transito'
        unique_together = (('conciliacionid', 'transaccionid'),)


class BancoConfigCheque(models.Model):
    bancocuentaid = models.IntegerField(primary_key=True)
    cheque_col = models.IntegerField(blank=True, null=True)
    cheque_lin = models.IntegerField(blank=True, null=True)
    dia_col = models.IntegerField(blank=True, null=True)
    dia_lin = models.IntegerField(blank=True, null=True)
    mes_col = models.IntegerField(blank=True, null=True)
    mes_lin = models.IntegerField(blank=True, null=True)
    ano_col = models.IntegerField(blank=True, null=True)
    ano_lin = models.IntegerField(blank=True, null=True)
    monto_letra_col = models.IntegerField(blank=True, null=True)
    monto_letra_lin = models.IntegerField(blank=True, null=True)
    monto_col = models.IntegerField(blank=True, null=True)
    monto_lin = models.IntegerField(blank=True, null=True)
    concepto_col = models.IntegerField(blank=True, null=True)
    concepto_lin = models.IntegerField(blank=True, null=True)
    benef_col = models.IntegerField(blank=True, null=True)
    benef_lin = models.IntegerField(blank=True, null=True)
    cuenta_col = models.IntegerField(blank=True, null=True)
    cuenta_lin = models.IntegerField(blank=True, null=True)
    cta_nombre_col = models.IntegerField(blank=True, null=True)
    cta_nombre_lin = models.IntegerField(blank=True, null=True)
    debito_col = models.IntegerField(blank=True, null=True)
    debito_lin = models.IntegerField(blank=True, null=True)
    credito_col = models.IntegerField(blank=True, null=True)
    credito_lin = models.IntegerField(blank=True, null=True)
    fecha_col = models.IntegerField(blank=True, null=True)
    fecha_lin = models.IntegerField(blank=True, null=True)
    monto_concepto_col = models.IntegerField(blank=True, null=True)
    monto_concepto_lin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_config_cheque'


class BancoCuenta(models.Model):
    bancocuentaid = models.AutoField(primary_key=True)
    bancoid = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    balance_minimo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sobregiro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_cuenta'


class BancoCuentaBalance(models.Model):
    balanceid = models.AutoField(primary_key=True)
    bancocuentaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_cuenta_balance'


class BancoNotacredito(models.Model):
    notacreditobancoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    hora = models.DateTimeField()
    bancoid = models.IntegerField()
    bancocuentaid = models.IntegerField()
    cuenta_numero = models.CharField(max_length=30, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    ncf = models.CharField(max_length=19, blank=True, null=True)
    ncf_modifica = models.CharField(max_length=19, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    estatus = models.CharField(max_length=3)
    bienid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banco_notacredito'


class BancoSolicitud(models.Model):
    solicitudid = models.AutoField(primary_key=True)
    bancoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    proveedorid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bancocuentaid = models.IntegerField(blank=True, null=True)
    cuenta_numero = models.CharField(max_length=30, blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aprobado_usuario = models.IntegerField(blank=True, null=True)
    aprobado_fecha = models.DateTimeField(blank=True, null=True)
    aprobado_hora = models.DateTimeField(blank=True, null=True)
    procesado_usuario = models.IntegerField(blank=True, null=True)
    procesado_fecha = models.DateTimeField(blank=True, null=True)
    procesado_hora = models.DateTimeField(blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True)
    nominaid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    cuenta_tipo = models.CharField(max_length=2, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    emergenciaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_solicitud'


class BancoSolicitudCaja(models.Model):
    solicitudid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_solicitud_caja'
        unique_together = (('solicitudid', 'detalleid'),)


class BancoSolicitudFactura(models.Model):
    solicitudid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    facturacxpid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pendiente = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    retencion_isr = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    retencion_itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    desembolsoid = models.IntegerField(blank=True, null=True)
    notadebitocxpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_solicitud_factura'
        unique_together = (('solicitudid', 'detalleid'),)


class BancoTransaccion(models.Model):
    transaccionid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    bancocuentaid = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    cuenta_numero = models.CharField(max_length=30, blank=True, null=True)
    cuenta_tipo = models.CharField(max_length=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    numero = models.IntegerField(blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    conciliado = models.IntegerField(blank=True, null=True)
    conciliacionid = models.IntegerField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    solicitudid = models.IntegerField(blank=True, null=True)
    fecha_conciliado = models.DateTimeField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_transaccion'


class BancoTransaccionCaja(models.Model):
    transaccionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_transaccion_caja'
        unique_together = (('transaccionid', 'detalleid'),)


class BancoTransaccionFactura(models.Model):
    transaccionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    facturacxpid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pendiente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    retencion_isr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    retencion_itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    desembolsoid = models.IntegerField(blank=True, null=True)
    notadebitocxpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_transaccion_factura'
        unique_together = (('transaccionid', 'detalleid'),)


class BancoTransaccionRecibo(models.Model):
    transaccionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    reciboid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_transaccion_recibo'
        unique_together = (('transaccionid', 'detalleid'),)


class Bien(models.Model):
    bienid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bien'


class Cafeteria(models.Model):
    cafeteriaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    formapago = models.CharField(max_length=2, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    tarjeta_numero = models.CharField(max_length=10, blank=True, null=True)
    tarjeta_autorizacion = models.CharField(max_length=10, blank=True, null=True)
    recibido = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    devuelta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    porc_cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medico = models.CharField(max_length=100, blank=True, null=True)
    fecha_receta = models.DateTimeField(blank=True, null=True)
    forma_autoriza = models.CharField(max_length=1, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    nombre_seguro = models.CharField(max_length=100, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porc_descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    anula_usuario = models.IntegerField(blank=True, null=True)
    anula_fecha = models.DateTimeField(blank=True, null=True)
    anula_hora = models.DateTimeField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    devolucion = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    devolucionid = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cuotas = models.IntegerField(blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    estatusid = models.IntegerField(blank=True, null=True)
    tipoglosaid = models.IntegerField(blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota_concurrencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    detalle_incidencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipoincidenciaid = models.IntegerField(blank=True, null=True)
    auditoria_glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    cierreid = models.IntegerField(blank=True, null=True)
    domicilio = models.IntegerField()
    domicilio_telefono = models.CharField(max_length=10, blank=True, null=True)
    domicilio_nombre = models.CharField(max_length=100, blank=True, null=True)
    domicilio_direccion1 = models.CharField(max_length=100, blank=True, null=True)
    domicilio_direccion2 = models.CharField(max_length=100, blank=True, null=True)
    domicilio_repartidor = models.CharField(max_length=100, blank=True, null=True)
    domicilio_referencia_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cafeteria'


class CafeteriaDetalle(models.Model):
    cafeteriaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis_venta = models.IntegerField()
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cafeteria_detalle'
        unique_together = (('cafeteriaid', 'detalleid'),)


class CafeteriaPago(models.Model):
    pagoid = models.AutoField(primary_key=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cafeteria_pago'


class CalendarioEpi(models.Model):
    calendarioid = models.AutoField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    semana = models.IntegerField(blank=True, null=True)
    mes_desde = models.IntegerField(blank=True, null=True)
    mes_hasta = models.IntegerField(blank=True, null=True)
    dia_desde = models.IntegerField(blank=True, null=True)
    dia_hasta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendario_epi'


class CalendarioMedicacion(models.Model):
    calendariomedicacionid = models.AutoField(primary_key=True)
    frecuenciaid = models.IntegerField()
    hora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'calendario_medicacion'


class CamaTipo(models.Model):
    tipocamaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cama_tipo'


class Catalogo(models.Model):
    cuentaid = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    controlid = models.CharField(max_length=15, blank=True, null=True)
    presupuesto = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    detalle = models.IntegerField(blank=True, null=True)
    origen = models.CharField(max_length=1, blank=True, null=True)
    balance_inicial = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha_balance_inicial = models.DateTimeField(blank=True, null=True)
    entrada_directa = models.IntegerField(blank=True, null=True)
    origen_recibe = models.CharField(max_length=1, blank=True, null=True)
    dimension = models.IntegerField(blank=True, null=True)
    caja_chica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'


class CatalogoEntrada(models.Model):
    entradaid = models.AutoField(primary_key=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    reciboid = models.IntegerField(blank=True, null=True)
    desembolsoid = models.IntegerField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    factura_prod = models.IntegerField(blank=True, null=True)
    glosaid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    nominaid = models.IntegerField(blank=True, null=True)
    regaliaid = models.IntegerField(blank=True, null=True)
    origen = models.CharField(max_length=1, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    facturacxpid = models.IntegerField(blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    diarioid = models.IntegerField(blank=True, null=True)
    solicitudid = models.IntegerField(blank=True, null=True)
    gastoid = models.IntegerField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    notacxpid = models.IntegerField(blank=True, null=True)
    notacreditoid = models.IntegerField(blank=True, null=True)
    devolucionid = models.IntegerField(blank=True, null=True)
    despachoid = models.IntegerField(blank=True, null=True)
    transferenciaid = models.IntegerField(blank=True, null=True)
    notadebitoid = models.IntegerField(blank=True, null=True)
    salidaid = models.IntegerField(blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    opcreciboid = models.IntegerField(blank=True, null=True)
    notadebitocxpid = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    notacreditobancoid = models.IntegerField(blank=True, null=True)
    dimensionid_detalle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_entrada'


class CategoriaActivo(models.Model):
    categoriaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cuentaid_activo = models.CharField(max_length=15)
    cuentaid_depreciacion = models.CharField(max_length=15)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'categoria_activo'


class Causa(models.Model):
    causaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    uso = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'causa'


class Certificado(models.Model):
    certificadoid = models.AutoField(primary_key=True)
    medicoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    resultado = models.TextField(blank=True, null=True)  # This field type is a guess.
    recomendacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    dias_incapacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificado'


class Cie10Grupo(models.Model):
    grupoid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=2000, blank=True, null=True)
    desde = models.CharField(max_length=5, blank=True, null=True)
    hasta = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cie10_grupo'


class Cie10Subgrupo(models.Model):
    grupoid = models.IntegerField(primary_key=True)
    subgrupoid = models.IntegerField()
    nombre = models.CharField(max_length=2000, blank=True, null=True)
    desde = models.CharField(max_length=5, blank=True, null=True)
    hasta = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cie10_subgrupo'
        unique_together = (('grupoid', 'subgrupoid'),)


class CierreAno(models.Model):
    cierreid = models.AutoField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cerrado = models.IntegerField(blank=True, null=True)
    diarioid = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cierre_ano'


class CierreCaja(models.Model):
    cierreid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid_caja = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    recibo_desde = models.IntegerField(blank=True, null=True)
    recibo_hasta = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    recibo_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recibo_tarjeta = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recibo_otros = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    desem_paciente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    desem_otro = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cierre_caja'


class CierreMes(models.Model):
    cierreid = models.AutoField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cerrado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cierre_mes'


class Cita(models.Model):
    citaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    completada = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    noshow = models.IntegerField()
    consultaid = models.ForeignKey('Consulta', models.DO_NOTHING, db_column='consultaid', blank=True, null=True)
    tipoatencionid = models.ForeignKey('TipoAtencion', models.DO_NOTHING, db_column='tipoatencionid', blank=True, null=True)
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'


class Cita1(models.Model):
    citaid = models.AutoField(primary_key=True)
    pacienteid = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='pacienteid', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medicoid', blank=True, null=True)
    completada = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    cita_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita1'


class Cliente(models.Model):
    clienteid = models.AutoField(primary_key=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    contacto_venta_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_venta_telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto_cobro_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_cobro_telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto_legal_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_legal_telefono = models.CharField(max_length=20, blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    limite = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    condicionid = models.IntegerField(blank=True, null=True)
    contacto_venta_correo = models.CharField(max_length=100, blank=True, null=True)
    contacto_cobro_correo = models.CharField(max_length=100, blank=True, null=True)
    contacto_legal_correo = models.CharField(max_length=100, blank=True, null=True)
    tipoclienteid = models.IntegerField(blank=True, null=True)
    envio_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    envio_telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    compraid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis_moneda = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento_moneda = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monto_moneda = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    facturada = models.IntegerField(blank=True, null=True)
    anticipo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    entradaid = models.IntegerField(blank=True, null=True)
    autorizacion_requiere_1 = models.IntegerField(blank=True, null=True)
    autorizacion_requiere_2 = models.IntegerField(blank=True, null=True)
    autorizacion_requiere_3 = models.IntegerField(blank=True, null=True)
    autorizacion_usuarioid_1 = models.IntegerField(blank=True, null=True)
    autorizacion_usuarioid_2 = models.IntegerField(blank=True, null=True)
    autorizacion_usuarioid_3 = models.IntegerField(blank=True, null=True)
    autorizacion_fecha_1 = models.DateTimeField(blank=True, null=True)
    autorizacion_fecha_2 = models.DateTimeField(blank=True, null=True)
    autorizacion_fecha_3 = models.DateTimeField(blank=True, null=True)
    autorizacion_hora_1 = models.DateTimeField(blank=True, null=True)
    autorizacion_hora_2 = models.DateTimeField(blank=True, null=True)
    autorizacion_hora_3 = models.DateTimeField(blank=True, null=True)
    usuarioid_reversa = models.IntegerField(blank=True, null=True)
    reversa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'compra'


class CompraAutoriza(models.Model):
    compraid = models.IntegerField(primary_key=True)
    usuarioid = models.IntegerField()
    estatus = models.CharField(max_length=3, blank=True, null=True)
    fecha_autoriza = models.DateTimeField(blank=True, null=True)
    hora_autoriza = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra_autoriza'
        unique_together = (('compraid', 'usuarioid'),)


class CompraConfig(models.Model):
    configid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    monto_desde = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monto_hasta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    usuarioid_1 = models.IntegerField(blank=True, null=True)
    usuarioid_2 = models.IntegerField(blank=True, null=True)
    usuarioid_3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra_config'


class CompraDetalle(models.Model):
    compraid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad_recibido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cod_barra = models.CharField(max_length=20, blank=True, null=True)
    serviciogeneralid = models.IntegerField(blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo = models.IntegerField(blank=True, null=True)
    acuerdo_cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo_oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo_costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad_pendiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad_facturado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra_detalle'
        unique_together = (('compraid', 'detalleid'),)


class Concepto(models.Model):
    conceptoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    referencia = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concepto'


class ConceptoAuditoriaMedica(models.Model):
    conceptoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concepto_auditoria_medica'


class Condicion(models.Model):
    condicionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condicion'


class ConfigAutorizacionCompra(models.Model):
    autorizacionid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    desde = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    hasta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid_1 = models.IntegerField(blank=True, null=True)
    usuarioid_2 = models.IntegerField(blank=True, null=True)
    usuarioid_3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_autorizacion_compra'


class Consulta(models.Model):
    consultaid = models.AutoField(primary_key=True)
    medicoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    atencion_inicio = models.DateTimeField(blank=True, null=True)
    atencion_fin = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    facturable = models.IntegerField(blank=True, null=True)
    tipoatencionid = models.IntegerField(blank=True, null=True)
    revisado = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'


class ConsultaEstudio(models.Model):
    recetaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    cuestionarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_estudio'


class ConsultaEstudioDetalle(models.Model):
    recetaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_estudio_detalle'
        unique_together = (('recetaid', 'detalleid'),)


class ConsultaHistoria(models.Model):
    historiaid = models.AutoField(primary_key=True)
    consultaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    anamnesis = models.TextField(blank=True, null=True)  # This field type is a guess.
    exploracion = models.TextField(blank=True, null=True)  # This field type is a guess.
    diagnostico = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento = models.TextField(blank=True, null=True)  # This field type is a guess.
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fc = models.CharField(max_length=10, blank=True, null=True)
    fr = models.CharField(max_length=10, blank=True, null=True)
    so = models.CharField(max_length=10, blank=True, null=True)
    temperatura = models.CharField(max_length=10, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    altura = models.CharField(max_length=10, blank=True, null=True)
    cabeza = models.CharField(max_length=10, blank=True, null=True)
    imc = models.CharField(max_length=10, blank=True, null=True)
    ps = models.CharField(max_length=10, blank=True, null=True)
    tipoatencionid = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    fc_fetal = models.CharField(max_length=10, blank=True, null=True)
    altura_uterina = models.CharField(max_length=10, blank=True, null=True)
    edema = models.CharField(max_length=1, blank=True, null=True)
    movimientos_fetales = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_historia'


class ConsultaInforme(models.Model):
    informeid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha = models.DateTimeField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    consultaid = models.IntegerField(blank=True, null=True)
    historiaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_informe'


class ConsultaInterconsulta(models.Model):
    interconsultaid = models.AutoField(primary_key=True)
    consultaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    hallazgos = models.TextField(blank=True, null=True)  # This field type is a guess.
    recomendacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    diagnostico = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consulta_interconsulta'


class ConsultaPatronEstudio(models.Model):
    patronid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_patron_estudio'


class ConsultaPatronEstudioDetalle(models.Model):
    patronid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consulta_patron_estudio_detalle'
        unique_together = (('patronid', 'detalleid'),)


class ConsultaPatronReceta(models.Model):
    patronid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_patron_receta'


class ConsultaPatronRecetaDetalle(models.Model):
    patronid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'consulta_patron_receta_detalle'
        unique_together = (('patronid', 'detalleid'),)


class ConsultaReceta(models.Model):
    recetaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    receta = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_receta'


class ConsultaRecetaDetalle(models.Model):
    recetaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_receta_detalle'
        unique_together = (('recetaid', 'detalleid'),)


class ConsultaSignosVitales(models.Model):
    signosid = models.AutoField(primary_key=True)
    consultaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    ps = models.CharField(max_length=10, blank=True, null=True)
    fc = models.CharField(max_length=10, blank=True, null=True)
    fr = models.CharField(max_length=10, blank=True, null=True)
    so = models.CharField(max_length=10, blank=True, null=True)
    temperatura = models.CharField(max_length=10, blank=True, null=True)
    peso = models.CharField(max_length=10, blank=True, null=True)
    talla = models.CharField(max_length=10, blank=True, null=True)
    altura = models.CharField(max_length=10, blank=True, null=True)
    cabeza = models.CharField(max_length=10, blank=True, null=True)
    fc_fetal = models.CharField(max_length=10, blank=True, null=True)
    altura_uterina = models.CharField(max_length=10, blank=True, null=True)
    edema = models.CharField(max_length=1, blank=True, null=True)
    movimientos_fetales = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_signos_vitales'


class ConsultaTurno(models.Model):
    turnoid = models.AutoField(primary_key=True)
    vacio = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_turno'


class Consultorio(models.Model):
    consultorioid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    pecio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultorio'


class ConsultorioCargo(models.Model):
    consultorioid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultorio_cargo'
        unique_together = (('consultorioid', 'detalleid'),)


class ConsultorioFactura(models.Model):
    facturaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    consultorioid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultorio_factura'


class ConsultorioFacturaDetalle(models.Model):
    facturaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultorio_factura_detalle'
        unique_together = (('facturaid', 'detalleid'),)


class ContConfigSituacion(models.Model):
    cuentaid = models.CharField(primary_key=True, max_length=15)
    nivel = models.IntegerField(blank=True, null=True)
    negrita = models.CharField(max_length=1, blank=True, null=True)
    subtotal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cont_config_situacion'


class ContConfigSituacionDetalle(models.Model):
    cuentaid = models.CharField(primary_key=True, max_length=15)
    cuentaid_suma = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'cont_config_situacion_detalle'
        unique_together = (('cuentaid', 'cuentaid_suma'),)


class CopiaCie10(models.Model):
    #c�digo = models.CharField(db_column='C�digo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #descripci�n = models.CharField(db_column='Descripci�n', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'copia_cie10'


class CopiaEmpleados(models.Model):
    cod = models.CharField(db_column='COD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apelido = models.CharField(max_length=255, blank=True, null=True)
    nomina = models.CharField(db_column='NOMINA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    concepto = models.CharField(db_column='CONCEPTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='CARGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ingreso = models.DateTimeField(blank=True, null=True)
    cuenta = models.FloatField(blank=True, null=True)
    nacimiento = models.DateTimeField(db_column='NACIMIENTO', blank=True, null=True)  # Field name made lowercase.
    edad = models.FloatField(db_column='EDAD', blank=True, null=True)  # Field name made lowercase.
    sueldo = models.FloatField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sexo = models.CharField(db_column='SEXO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='TELEFONOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'copia_empleados'


class CopiaProductos(models.Model):
    proveedor = models.CharField(db_column='PROVEEDOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rnc = models.FloatField(db_column='RNC', blank=True, null=True)  # Field name made lowercase.
    almacen = models.FloatField(db_column='ALMACEN', blank=True, null=True)  # Field name made lowercase.
    servicio = models.CharField(db_column='SERVICIO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    costo = models.FloatField(db_column='COSTO', blank=True, null=True)  # Field name made lowercase.
    existencia = models.FloatField(db_column='EXISTENCIA', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'copia_productos'


class Correos(models.Model):
    correoid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correos'


class Cotizacion(models.Model):
    cotizacionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    medicamentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estudios = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    seguroid = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2)
    razonid_descuento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizacion'


class CotizacionEstudio(models.Model):
    cotizacionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    codigo_seguro = models.CharField(max_length=6, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizacion_estudio'
        unique_together = (('cotizacionid', 'detalleid'),)


class CotizacionHonorario(models.Model):
    cotizacionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizacion_honorario'
        unique_together = (('cotizacionid', 'detalleid'),)


class CotizacionProducto(models.Model):
    cotizacionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cotizacion_producto'
        unique_together = (('cotizacionid', 'detalleid'),)


class CuestionarioConfig(models.Model):
    cuestionarioid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    momento = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cuestionario_config'


class CuestionarioConfigDetaiile(models.Model):
    cuestionarioid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    pregunta = models.CharField(max_length=100, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuestionario_config_detaiile'
        unique_together = (('cuestionarioid', 'detalleid'),)


class CuestionarioConfigDetaiileEstudio(models.Model):
    cuestionarioid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cuestionario_config_detaiile_estudio'
        unique_together = (('cuestionarioid', 'detalleid', 'estudioid'),)


class Cxc(models.Model):
    cxcid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    notadebitoid = models.IntegerField(blank=True, null=True)
    glosaid = models.IntegerField(blank=True, null=True)
    reciboid = models.IntegerField(blank=True, null=True)
    notacreditoid = models.IntegerField(blank=True, null=True)
    factura_prod = models.IntegerField(blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cxc'


class CxcMedico(models.Model):
    cxcid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    factruraid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    consultorioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cxc_medico'


class Cxp(models.Model):
    cxpid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    facturacxpid = models.IntegerField(blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    devolucionid = models.IntegerField(blank=True, null=True)
    notacxpid = models.IntegerField(blank=True, null=True)
    desembolsoid = models.IntegerField(blank=True, null=True)
    notadebitocxpid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cxp'


class CxpHonorario(models.Model):
    honorarioid = models.AutoField(primary_key=True)
    medicoid = models.IntegerField(blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    monto_factura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    desembolsoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cxp_honorario'


class Departamento(models.Model):
    departamentoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    autoriza = models.IntegerField(blank=True, null=True)
    confirmar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DepartamentoAutoriza(models.Model):
    departamentoid = models.IntegerField(primary_key=True)
    rolid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'departamento_autoriza'
        unique_together = (('departamentoid', 'rolid'),)


class DepartamentoCuenta(models.Model):
    departamentoid = models.IntegerField(primary_key=True)
    tipoingresoid = models.IntegerField()
    tipodescuentoid = models.IntegerField()
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento_cuenta'
        unique_together = (('departamentoid', 'tipoingresoid', 'tipodescuentoid'),)


class DepartamentoServicio(models.Model):
    departamentoid = models.IntegerField(primary_key=True)
    servicioid = models.IntegerField()
    cuentaid_inv = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_cos = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento_servicio'
        unique_together = (('departamentoid', 'servicioid'),)


class Descuento(models.Model):
    descuentoid = models.AutoField(primary_key=True)
    servicioid = models.IntegerField()
    desde = models.DateTimeField()
    hasta = models.DateTimeField()
    tipo = models.CharField(max_length=1)
    porciento = models.DecimalField(max_digits=10, decimal_places=2)
    estatus = models.CharField(max_length=3)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipopacienteid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descuento'


class Desembolso(models.Model):
    desembolsoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioautoriza = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    gastoid = models.IntegerField(blank=True, null=True)
    gasto_menor = models.IntegerField(blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    cierreid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)
    propina = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_servicio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    dimension = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desembolso'


class DesembolsoFactura(models.Model):
    desembolsoid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    facturacxpid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pendiente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desembolso_factura'
        unique_together = (('desembolsoid', 'detalleid'),)


class DesembolsoTipoCierre(models.Model):
    tipo = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'desembolso_tipo_cierre'


class Despacho(models.Model):
    despachoid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3)
    hora = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_autoriza = models.IntegerField(blank=True, null=True)
    departamentoid_autoriza = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'despacho'


class DespachoDetalle(models.Model):
    despachoid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    alto_riesgo = models.CharField(max_length=1, blank=True, null=True)
    precio_cero = models.IntegerField(blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'despacho_detalle'
        unique_together = (('despachoid', 'detalleid'),)


class Devolucion(models.Model):
    devolucionid = models.AutoField(primary_key=True)
    servicioid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    ncf_modifica = models.CharField(max_length=20, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    proveedorid = models.IntegerField(blank=True, null=True)
    facturacxpid = models.IntegerField(blank=True, null=True)
    facturaid = models.CharField(max_length=20, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    despachoid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    ordenid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'devolucion'


class DevolucionDetalle(models.Model):
    devolucionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'devolucion_detalle'
        unique_together = (('devolucionid', 'detalleid'),)


class Diagnostico(models.Model):
    cie10 = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnostico'


class Diario(models.Model):
    diarioid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    cierre = models.IntegerField(blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diario'


class Dieta(models.Model):
    dietaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    desayuno_hora = models.DateTimeField(blank=True, null=True)
    desayuno_texto = models.TextField(blank=True, null=True)  # This field type is a guess.
    comida_hora = models.DateTimeField(blank=True, null=True)
    comida_texto = models.TextField(blank=True, null=True)  # This field type is a guess.
    cena_hora = models.DateTimeField(blank=True, null=True)
    cena_texto = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dieta'


class Dimension(models.Model):
    dimensionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dimension'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Doppler(models.Model):
    dopplerid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doppler'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Ecocardiograma(models.Model):
    ecoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecocardiograma'


class Emergencia(models.Model):
    emergenciaid = models.AutoField(primary_key=True)
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    poliza = models.CharField(max_length=20, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    ingresado = models.CharField(max_length=5, blank=True, null=True)
    referido = models.CharField(max_length=5, blank=True, null=True)
    alta = models.CharField(max_length=5, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    resp_nombre = models.CharField(max_length=80, blank=True, null=True)
    resp_telefono = models.CharField(max_length=30, blank=True, null=True)
    resp_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    parentescoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    autorizacionid = models.IntegerField(blank=True, null=True)
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    glosa = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    resp_cedula = models.CharField(max_length=20, blank=True, null=True)
    certificadoid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    entregada = models.IntegerField(blank=True, null=True)
    usuarioid_entregada = models.IntegerField(blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    triaje_nivel = models.CharField(max_length=20, blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    cubiculo = models.CharField(max_length=10, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    hora_factura = models.DateTimeField(blank=True, null=True)
    auditoria_nota_medica = models.CharField(max_length=2000, blank=True, null=True)
    honorarioid = models.IntegerField(blank=True, null=True)
    estatusid = models.IntegerField(blank=True, null=True)
    tipoglosaid = models.IntegerField(blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota_concurrencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    detalle_incidencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipoincidenciaid = models.IntegerField(blank=True, null=True)
    fecha_entrega_seguro = models.DateTimeField(blank=True, null=True)
    fecha_recibe_seguro = models.DateTimeField(blank=True, null=True)
    fecha_entrega_auditor = models.DateTimeField(blank=True, null=True)
    fecha_recepcion_auditor = models.DateTimeField(blank=True, null=True)
    auditoria_glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    auditoria_observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    auditorid_medico = models.IntegerField(blank=True, null=True)
    fecha_primera_atencion = models.DateTimeField(blank=True, null=True)
    hora_primera_atencion = models.DateTimeField(blank=True, null=True)
    facturaintid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    resp_parentesco = models.CharField(max_length=50, blank=True, null=True)
    servicio_integracion_usuario = models.CharField(max_length=20, blank=True, null=True)
    servicio_integracion_clave = models.CharField(max_length=10, blank=True, null=True)
    usuarioid_cobertura_disponible = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia'


class EmergenciaAdmision(models.Model):
    emergenciaid = models.IntegerField(primary_key=True)
    fuente_informacion = models.CharField(max_length=50, blank=True, null=True)
    entrega_nombre = models.CharField(max_length=100, blank=True, null=True)
    entrega_telefono = models.CharField(max_length=20, blank=True, null=True)
    motivo = models.CharField(max_length=200, blank=True, null=True)
    evento_lugar = models.CharField(max_length=100, blank=True, null=True)
    evento_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    evento_fecha = models.DateTimeField(blank=True, null=True)
    evento_hora = models.DateTimeField(blank=True, null=True)
    evento_arma = models.CharField(max_length=50, blank=True, null=True)
    denuncia_autoridad = models.CharField(max_length=100, blank=True, null=True)
    denuncia_hora = models.DateTimeField(blank=True, null=True)
    denuncia_observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    picadura = models.CharField(max_length=100, blank=True, null=True)
    mordedura = models.CharField(max_length=100, blank=True, null=True)
    antecedentes_1 = models.CharField(max_length=200, blank=True, null=True)
    antecedentes_2 = models.CharField(max_length=200, blank=True, null=True)
    antecedentes_3 = models.CharField(max_length=200, blank=True, null=True)
    enfermedad_1 = models.CharField(max_length=200, blank=True, null=True)
    enfermedad_2 = models.CharField(max_length=200, blank=True, null=True)
    enfermedad_3 = models.CharField(max_length=200, blank=True, null=True)
    enfermedad_4 = models.CharField(max_length=200, blank=True, null=True)
    dolor_region_1 = models.CharField(max_length=50, blank=True, null=True)
    dolor_region_2 = models.CharField(max_length=50, blank=True, null=True)
    dolor_region_3 = models.CharField(max_length=50, blank=True, null=True)
    dolor_punto_1 = models.CharField(max_length=50, blank=True, null=True)
    dolor_punto_2 = models.CharField(max_length=50, blank=True, null=True)
    dolor_punto_3 = models.CharField(max_length=50, blank=True, null=True)
    dolor_intencidad_1 = models.CharField(max_length=10, blank=True, null=True)
    dolor_intencidad_2 = models.CharField(max_length=10, blank=True, null=True)
    dolor_intencidad_3 = models.CharField(max_length=10, blank=True, null=True)
    forma_llegada = models.CharField(max_length=1, blank=True, null=True)
    via_aerea = models.CharField(max_length=1, blank=True, null=True)
    condicion_llegada = models.CharField(max_length=1, blank=True, null=True)
    condicion_otro = models.CharField(max_length=100, blank=True, null=True)
    evento_tipo = models.CharField(max_length=1, blank=True, null=True)
    quemadura_grado = models.CharField(max_length=1, blank=True, null=True)
    quemadura_superficie = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    denuncia_custodia = models.IntegerField(blank=True, null=True)
    dolor_agudo_1 = models.IntegerField(blank=True, null=True)
    dolor_agudo_2 = models.IntegerField(blank=True, null=True)
    dolor_agudo_3 = models.IntegerField(blank=True, null=True)
    dolor_subagudo_1 = models.IntegerField(blank=True, null=True)
    dolor_subagudo_2 = models.IntegerField(blank=True, null=True)
    dolor_subagudo_3 = models.IntegerField(blank=True, null=True)
    dolor_cronico_1 = models.IntegerField(blank=True, null=True)
    dolor_cronico_2 = models.IntegerField(blank=True, null=True)
    dolor_cronico_3 = models.IntegerField(blank=True, null=True)
    dolor_episodio_1 = models.IntegerField(blank=True, null=True)
    dolor_episodio_2 = models.IntegerField(blank=True, null=True)
    dolor_episodio_3 = models.IntegerField(blank=True, null=True)
    dolor_continuo_1 = models.IntegerField(blank=True, null=True)
    dolor_continuo_2 = models.IntegerField(blank=True, null=True)
    dolor_continuo_3 = models.IntegerField(blank=True, null=True)
    dolor_antiesp_1 = models.IntegerField(blank=True, null=True)
    dolor_antiesp_2 = models.IntegerField(blank=True, null=True)
    dolor_antiesp_3 = models.IntegerField(blank=True, null=True)
    dolor_opiaseo_1 = models.IntegerField(blank=True, null=True)
    dolor_opiaseo_2 = models.IntegerField(blank=True, null=True)
    dolor_opiaseo_3 = models.IntegerField(blank=True, null=True)
    dolor_alivia_1 = models.IntegerField(blank=True, null=True)
    dolor_alivia_2 = models.IntegerField(blank=True, null=True)
    dolor_alivia_3 = models.IntegerField(blank=True, null=True)
    dolor_colico_1 = models.IntegerField(blank=True, null=True)
    dolor_colico_2 = models.IntegerField(blank=True, null=True)
    dolor_colico_3 = models.IntegerField(blank=True, null=True)
    dolor_aine_1 = models.IntegerField(blank=True, null=True)
    dolor_aine_2 = models.IntegerField(blank=True, null=True)
    dolor_aine_3 = models.IntegerField(blank=True, null=True)
    signos_pa = models.CharField(db_column='signos_PA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    signos_fc = models.DecimalField(db_column='signos_FC', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signos_fr = models.DecimalField(db_column='signos_FR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    signos_temp_bucal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_temp_axilar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_talla = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_perim_cefalico = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_glasgow_ocular = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_glasgow_verbal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_glasgow_motora = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    signos_glasgow_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reaccion_pupila_der = models.CharField(max_length=10, blank=True, null=True)
    reaccion_pupila_izq = models.CharField(max_length=10, blank=True, null=True)
    reaccion_llenado_capilar = models.CharField(max_length=10, blank=True, null=True)
    fisico_piel = models.IntegerField(blank=True, null=True)
    fisico_capeza = models.IntegerField(blank=True, null=True)
    fisico_ojos = models.IntegerField(blank=True, null=True)
    fisico_oidos = models.IntegerField(blank=True, null=True)
    fisico_nariz = models.IntegerField(blank=True, null=True)
    fisico_boca = models.IntegerField(blank=True, null=True)
    fisico_orofaringe = models.IntegerField(blank=True, null=True)
    fisico_cuello = models.IntegerField(blank=True, null=True)
    fisico_axilasmamas = models.IntegerField(blank=True, null=True)
    fisico_torax = models.IntegerField(blank=True, null=True)
    fisico_abdomen = models.IntegerField(blank=True, null=True)
    fisico_columna = models.IntegerField(blank=True, null=True)
    fisico_ingle = models.IntegerField(blank=True, null=True)
    fisico_miembros_sup = models.IntegerField(blank=True, null=True)
    fisico_miembros_inf = models.IntegerField(blank=True, null=True)
    fisico_organosentidos = models.IntegerField(blank=True, null=True)
    fisico_respiratorio = models.IntegerField(blank=True, null=True)
    fisico_cardiovascular = models.IntegerField(blank=True, null=True)
    fisico_digestivo = models.IntegerField(blank=True, null=True)
    fisico_genital = models.IntegerField(blank=True, null=True)
    fisico_urinario = models.IntegerField(blank=True, null=True)
    fisico_musculoesqueletico = models.IntegerField(blank=True, null=True)
    fisico_endocrino = models.IntegerField(blank=True, null=True)
    fisico_hemolinfatico = models.IntegerField(blank=True, null=True)
    fisico_neurologico = models.IntegerField(blank=True, null=True)
    fisico_linea1 = models.CharField(max_length=150, blank=True, null=True)
    fisico_linea2 = models.CharField(max_length=150, blank=True, null=True)
    fisico_linea3 = models.CharField(max_length=150, blank=True, null=True)
    fisico_linea4 = models.CharField(max_length=150, blank=True, null=True)
    diagrama_herida_permanente = models.IntegerField(blank=True, null=True)
    diagrama_herida_nopermanente = models.IntegerField(blank=True, null=True)
    diagrama_fractura_expuesta = models.IntegerField(blank=True, null=True)
    diagrama_fractura_noexpuesta = models.IntegerField(blank=True, null=True)
    diagrama_amputacion = models.IntegerField(blank=True, null=True)
    diagrama_hemorragia = models.IntegerField(blank=True, null=True)
    diagrama_mordedura = models.IntegerField(blank=True, null=True)
    diagrama_picadura = models.IntegerField(blank=True, null=True)
    diagrama_excoriacion = models.IntegerField(blank=True, null=True)
    diagrama_deformidad = models.IntegerField(blank=True, null=True)
    diagrama_hematoma = models.IntegerField(blank=True, null=True)
    embarazo_gestas = models.IntegerField(blank=True, null=True)
    embarazo_partos = models.IntegerField(blank=True, null=True)
    embarazo_abortos = models.IntegerField(blank=True, null=True)
    embarazo_cesareas = models.IntegerField(blank=True, null=True)
    embarazo_ult_mestruacion = models.DateTimeField(blank=True, null=True)
    embarazo_semanas_gest = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_movimiento_fetal = models.IntegerField(blank=True, null=True)
    embarazo_frecuencia_fetal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_membranas_rotas = models.IntegerField(blank=True, null=True)
    embarazo_tiempo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_altura_uterina = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_presenta_con = models.CharField(max_length=20, blank=True, null=True)
    embarazo_dilatacion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_borramiento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_pelvis = models.IntegerField(blank=True, null=True)
    embarazo_sangrado = models.IntegerField(blank=True, null=True)
    embarazo_contracciones = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    embarazo_linea1 = models.CharField(max_length=80, blank=True, null=True)
    embarazo_linea2 = models.CharField(max_length=80, blank=True, null=True)
    analisis_problema_1 = models.CharField(max_length=80, blank=True, null=True)
    analisis_problema_2 = models.CharField(max_length=80, blank=True, null=True)
    analisis_problema_3 = models.CharField(max_length=80, blank=True, null=True)
    analisis_problema_4 = models.CharField(max_length=80, blank=True, null=True)
    analisis_problema_5 = models.CharField(max_length=80, blank=True, null=True)
    diagnostico_presuntivo_1 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_2 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_3 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_definitivo_1 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_definitivo_2 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_definitivo_3 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_cie10_1 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_presuntivo_cie10_2 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_presuntivo_cie10_3 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_definitivo_cie10_1 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_definitivo_cie10_2 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_definitivo_cie10_3 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_medicamento_1 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_2 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_3 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_4 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_via_1 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_2 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_3 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_4 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_dosis_1 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_2 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_3 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_4 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_1 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_2 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_3 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_4 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dias_1 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_2 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_3 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_4 = models.IntegerField(blank=True, null=True)
    tratamiento_indicacion_general = models.IntegerField(blank=True, null=True)
    tratamiento_procedimiento = models.IntegerField(blank=True, null=True)
    tratamiento_consentimiento = models.IntegerField(blank=True, null=True)
    tratamiento_otros = models.IntegerField(blank=True, null=True)
    tratamiento_linea1 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea2 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea3 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea4 = models.CharField(max_length=100, blank=True, null=True)
    antecedentes_alergicos = models.IntegerField(blank=True, null=True)
    antecedentes_clinicos = models.IntegerField(blank=True, null=True)
    antecedentes_ginecologicos = models.IntegerField(blank=True, null=True)
    antecedentes_traumatologicos = models.IntegerField(blank=True, null=True)
    antecedentes_pediatricos = models.IntegerField(blank=True, null=True)
    antecedentes_quirurgicos = models.IntegerField(blank=True, null=True)
    antecedentes_farmacologicos = models.IntegerField(blank=True, null=True)
    antecedentes_otros = models.IntegerField(blank=True, null=True)
    fisico_linea5 = models.CharField(max_length=150, blank=True, null=True)
    fisico_linea6 = models.CharField(max_length=150, blank=True, null=True)
    fisico_linea7 = models.CharField(max_length=300, blank=True, null=True)
    aconseja = models.TextField(blank=True, null=True)  # This field type is a guess.
    origen = models.CharField(max_length=60, blank=True, null=True)
    enfermedad_actual = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento_medicamento_5 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_6 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_7 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_medicamento_8 = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_via_5 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_6 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_7 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_via_8 = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_dosis_5 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_6 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_7 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dosis_8 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_5 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_6 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_7 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_posologia_8 = models.CharField(max_length=10, blank=True, null=True)
    tratamiento_dias_5 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_6 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_7 = models.IntegerField(blank=True, null=True)
    tratamiento_dias_8 = models.IntegerField(blank=True, null=True)
    tratamiento_linea5 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea6 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea7 = models.CharField(max_length=100, blank=True, null=True)
    tratamiento_linea8 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_4 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_5 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_definitivo_4 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_definitivo_5 = models.CharField(max_length=100, blank=True, null=True)
    diagnostico_presuntivo_cie10_4 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_presuntivo_cie10_5 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_definitivo_cie10_4 = models.CharField(max_length=10, blank=True, null=True)
    diagnostico_definitivo_cie10_5 = models.CharField(max_length=10, blank=True, null=True)
    signos_glicemia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_admision'


class EmergenciaAlta(models.Model):
    altaid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    salida_donde = models.CharField(max_length=1, blank=True, null=True)
    salida_condicion = models.CharField(max_length=1, blank=True, null=True)
    dias_incapacidad = models.IntegerField(blank=True, null=True)
    muerto = models.IntegerField(blank=True, null=True)
    causa_muerte = models.CharField(max_length=200, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    aconseja = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'emergencia_alta'


class EmergenciaAuditoria(models.Model):
    notaid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'emergencia_auditoria'


class EmergenciaEstudio(models.Model):
    emergenciaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    codigo_seguro = models.CharField(max_length=10, blank=True, null=True)
    enviado_laboratorio = models.IntegerField(blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    laboratorioid = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid_inserta = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    fecha_elimina = models.DateTimeField(blank=True, null=True)
    fecha_inserta = models.DateTimeField(blank=True, null=True)
    usuarioid_elimina = models.IntegerField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    exclusion_internacional = models.IntegerField(blank=True, null=True)
    simon = models.CharField(max_length=10, blank=True, null=True)
    validar_informe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emergencia_estudio'
        unique_together = (('emergenciaid', 'detalleid'),)


class EmergenciaFirma(models.Model):
    emergenciafirmaid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField()
    tipo = models.CharField(max_length=1)
    firma = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_firma'


class EmergenciaHonorario(models.Model):
    emergenciaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobrar = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_honorario'
        unique_together = (('emergenciaid', 'detalleid'),)


class EmergenciaHonorarioManual(models.Model):
    emergenciaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_honorario_manual'
        unique_together = (('emergenciaid', 'detalleid'),)


class EmergenciaInforme(models.Model):
    informeid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_informe'


class EmergenciaInterconsulta(models.Model):
    interconsultaid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    hallazgos = models.TextField(blank=True, null=True)  # This field type is a guess.
    recomendacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    diagnostico = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_interconsulta'


class EmergenciaLog(models.Model):
    logid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_log'


class EmergenciaMedicacion(models.Model):
    medicacionid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    productoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    nota_medica = models.TextField(blank=True, null=True)  # This field type is a guess.
    nota_enfermera = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'emergencia_medicacion'


class EmergenciaProducto(models.Model):
    emergenciaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'emergencia_producto'
        unique_together = (('emergenciaid', 'detalleid'),)


class EmergenciaSignosVitales(models.Model):
    signosid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    ta = models.CharField(max_length=15, blank=True, null=True)
    fc = models.CharField(max_length=15, blank=True, null=True)
    pulso = models.CharField(max_length=15, blank=True, null=True)
    temperatura = models.CharField(max_length=15, blank=True, null=True)
    fr = models.CharField(max_length=15, blank=True, null=True)
    diuresis = models.CharField(max_length=15, blank=True, null=True)
    estado_vigilia = models.CharField(max_length=20, blank=True, null=True)
    morse = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    so = models.CharField(max_length=15, blank=True, null=True)
    glicemia = models.CharField(max_length=20, blank=True, null=True)
    downton = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergencia_signos_vitales'


class Emergenciaint(models.Model):
    emergenciaintid = models.AutoField(primary_key=True)
    emergenciaid = models.IntegerField()
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    poliza = models.CharField(max_length=20, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    ingresado = models.CharField(max_length=5, blank=True, null=True)
    referido = models.CharField(max_length=5, blank=True, null=True)
    alta = models.CharField(max_length=5, blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    resp_nombre = models.CharField(max_length=80, blank=True, null=True)
    resp_telefono = models.CharField(max_length=30, blank=True, null=True)
    resp_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    parentescoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    autorizacionid = models.IntegerField(blank=True, null=True)
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    resp_cedula = models.CharField(max_length=20, blank=True, null=True)
    certificadoid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    entregada = models.IntegerField(blank=True, null=True)
    usuarioid_entregada = models.IntegerField(blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    triaje_nivel = models.CharField(max_length=20, blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    cubiculo = models.CharField(max_length=10, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    hora_factura = models.DateTimeField(blank=True, null=True)
    resp_parentesco = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergenciaint'


class EmergenciaintEstudio(models.Model):
    emergenciaintid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    codigo_seguro = models.CharField(max_length=10, blank=True, null=True)
    enviado_laboratorio = models.IntegerField(blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    laboratorioid = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergenciaint_estudio'
        unique_together = (('emergenciaintid', 'detalleid'),)


class EmergenciaintProducto(models.Model):
    emergenciaintid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergenciaint_producto'
        unique_together = (('emergenciaintid', 'detalleid'),)


class Empleado(models.Model):
    empleadoid = models.AutoField(primary_key=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    estadocivilid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    tiene_licencia = models.CharField(max_length=1, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    profesionid = models.IntegerField(blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cargoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=20, blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    banco_cuenta = models.CharField(max_length=50, blank=True, null=True)
    banco_cuenta_tipo = models.CharField(max_length=1, blank=True, null=True)
    empleadoid_supervisor = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    porc_limite_credito = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    usuarioid_empleado = models.IntegerField(blank=True, null=True)
    flota = models.CharField(max_length=30, blank=True, null=True)
    extension = models.CharField(max_length=30, blank=True, null=True)
    correo_institucion = models.CharField(max_length=100, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    execuatur = models.CharField(max_length=20, blank=True, null=True)
    afp = models.CharField(max_length=100, blank=True, null=True)
    genera_carta_isr = models.IntegerField()
    sueldo = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'empleado'


class EmpleadoAmonestacion(models.Model):
    amonestacionid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    empleadoid_amonesta = models.IntegerField(blank=True, null=True)
    motivoid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    reportado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_amonestacion'


class EmpleadoArchivo(models.Model):
    archivoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    tipoarchivoid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ruta = models.CharField(max_length=2000, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_archivo'


class EmpleadoAsistencia(models.Model):
    asistenciaid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    cargoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    fecha_archivo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_asistencia'


class EmpleadoCargo(models.Model):
    cargoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_cargo'


class EmpleadoCarta(models.Model):
    empleadoid = models.IntegerField(primary_key=True)
    cartaid = models.IntegerField()
    decalleid = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_carta'
        unique_together = (('empleadoid', 'cartaid', 'decalleid'),)


class EmpleadoCxc(models.Model):
    cxcid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    prestamoid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    nominaid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_cxc'


class EmpleadoDependiente(models.Model):
    dependienteid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    parentescoid = models.IntegerField(blank=True, null=True)
    fecha_nac = models.DateTimeField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    fecha_inclusion = models.DateTimeField(blank=True, null=True)
    nss = models.CharField(max_length=20, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    tss = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'empleado_dependiente'


class EmpleadoDescuento(models.Model):
    descuentoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    tipodescuentoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    periodo = models.CharField(max_length=1, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    fijo = models.IntegerField()
    dependienteid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_descuento'


class EmpleadoDescuentoExcluir(models.Model):
    excluirid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    tipodescuentoid = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_descuento_excluir'


class EmpleadoEmergencia(models.Model):
    emergenciaid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    parentescoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_emergencia'


class EmpleadoEquipo(models.Model):
    equipoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_equipo'


class EmpleadoEstudio(models.Model):
    estudioid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    institucion = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    patrocinado = models.CharField(max_length=1, blank=True, null=True)
    reembolsable = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_estudio'


class EmpleadoExperiencia(models.Model):
    experienciaid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    supervisor = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    motivo = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    sueldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_experiencia'


class EmpleadoFoto(models.Model):
    empleadoid = models.IntegerField(primary_key=True)
    foto = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_foto'


class EmpleadoHorasExtras(models.Model):
    extrasid = models.AutoField(primary_key=True)
    empleadoid = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleadoid')
    fecha = models.DateTimeField()
    tipoingresoid = models.ForeignKey('NominaTipoIngreso', models.DO_NOTHING, db_column='tipoingresoid')
    tipoid = models.ForeignKey('NominaTipo', models.DO_NOTHING, db_column='tipoid')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    monto_hora = models.DecimalField(max_digits=18, decimal_places=2)
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid', blank=True, null=True)
    nominaid = models.ForeignKey('Nomina', models.DO_NOTHING, db_column='nominaid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_horas_extras'


class EmpleadoIngreso(models.Model):
    ingresoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    tipoingresoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    periodo = models.CharField(max_length=1, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    fijo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado_ingreso'


class EmpleadoLicencia(models.Model):
    licenciaid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    motivoid = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha = models.DateTimeField(blank=True, null=True)
    accionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_licencia'


class EmpleadoMedico(models.Model):
    empleadoid = models.IntegerField(primary_key=True)
    medicamentos = models.TextField(blank=True, null=True)  # This field type is a guess.
    operaciones = models.TextField(blank=True, null=True)  # This field type is a guess.
    enfermedades = models.TextField(blank=True, null=True)  # This field type is a guess.
    antecedentes = models.TextField(blank=True, null=True)  # This field type is a guess.
    alergias = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'empleado_medico'


class EmpleadoNomina(models.Model):
    empleadoid = models.IntegerField(primary_key=True)
    tipoid = models.IntegerField()
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    sueldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sueldo_dia = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sueldo_hora = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    banco_cuenta = models.CharField(max_length=50, blank=True, null=True)
    forma_pago = models.CharField(max_length=1, blank=True, null=True)
    accionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    isr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_nomina'
        unique_together = (('empleadoid', 'tipoid'),)


class EmpleadoPermiso(models.Model):
    permisoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora_desde = models.DateTimeField(blank=True, null=True)
    hora_hasta = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    motivoid = models.IntegerField(blank=True, null=True)
    accionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_permiso'


class EmpleadoPrestamo(models.Model):
    prestamoid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cuota = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    periodo = models.CharField(max_length=1, blank=True, null=True)
    cantidad_cuotas = models.IntegerField(blank=True, null=True)
    tipodescuentoid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    revisado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_prestamo'


class EmpleadoTipo(models.Model):
    tipoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_tipo'


class EmpleadoVacacion(models.Model):
    vacacionid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    dias = models.IntegerField(blank=True, null=True)
    disfrutados = models.IntegerField(blank=True, null=True)
    solicito = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    fecha_reintegro = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    accionid = models.IntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=18, decimal_places=2)
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    tipoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    salario_dia = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'empleado_vacacion'


class EmpleadosImgFinal(models.Model):
    cedula = models.CharField(db_column='CEDULA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados_img_final'


class Empresa(models.Model):
    empresaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    rnc = models.CharField(max_length=11, blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    direccion1 = models.CharField(max_length=100, blank=True, null=True)
    direccion2 = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    empresancf = models.IntegerField(blank=True, null=True)
    servicio_emergencia = models.IntegerField(blank=True, null=True)
    almacen_emergencia = models.IntegerField(blank=True, null=True)
    causa_ingresado = models.IntegerField(blank=True, null=True)
    servicio_hospitalizacion = models.IntegerField(blank=True, null=True)
    estudio_hospitalizacion = models.IntegerField(blank=True, null=True)
    licencia = models.CharField(max_length=100, blank=True, null=True)
    nomina_idestablecimiento = models.IntegerField(blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    sello = models.BinaryField(blank=True, null=True)
    fondo = models.BinaryField(blank=True, null=True)
    logo_receta = models.BinaryField(blank=True, null=True)
    logo_internacional = models.BinaryField(blank=True, null=True)
    sms = models.IntegerField(blank=True, null=True)
    administrativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empresa'


class Encuesta(models.Model):
    encuestaid = models.AutoField(primary_key=True)
    preguntaid = models.IntegerField()
    servicioid = models.IntegerField()
    pregunta = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuesta'


class EncuestaPregunta(models.Model):
    encuestaid = models.IntegerField(primary_key=True)
    preguntaid = models.IntegerField()
    detalleid = models.IntegerField()
    respuesta = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuesta_pregunta'
        unique_together = (('encuestaid', 'preguntaid', 'detalleid'),)


class Endoscopia(models.Model):
    endoscopiaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    foto1 = models.BinaryField(blank=True, null=True)
    foto2 = models.BinaryField(blank=True, null=True)
    foto3 = models.BinaryField(blank=True, null=True)
    foto4 = models.BinaryField(blank=True, null=True)
    instrumento = models.CharField(max_length=50, blank=True, null=True)
    sedacion = models.CharField(max_length=50, blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endoscopia'


class Entrada(models.Model):
    entradaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    despachoid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    facturaid = models.CharField(max_length=20, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    formapagoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrada'


class EntradaDetalle(models.Model):
    entradaid = models.IntegerField()
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis_parte_costo = models.IntegerField()
    existencia_actual = models.DecimalField(max_digits=10, decimal_places=2)
    costo_actual = models.DecimalField(max_digits=18, decimal_places=2)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrada_detalle'


class Especialidad(models.Model):
    especialidadid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class EstadoGrid(models.Model):
    estadoid = models.AutoField(primary_key=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    pantalla = models.CharField(max_length=100, blank=True, null=True)
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    grid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_grid'


class Estadocivil(models.Model):
    estadocivilid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocivil'


class EstatusHabitacion(models.Model):
    estatusid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estatus_habitacion'


class Estudio(models.Model):
    estudioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    tipoestudioid = models.IntegerField(blank=True, null=True)
    codigo_seguro = models.CharField(max_length=20, blank=True, null=True)
    abreviatura = models.CharField(max_length=12, blank=True, null=True)
    seccionid = models.IntegerField(blank=True, null=True)
    tipomuestraid = models.IntegerField(blank=True, null=True)
    tipoenvaseid = models.IntegerField(blank=True, null=True)
    metodoid = models.IntegerField(blank=True, null=True)
    requisitoid = models.IntegerField(blank=True, null=True)
    horasresultado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quirurgico = models.CharField(max_length=1, blank=True, null=True)
    cups = models.CharField(max_length=10, blank=True, null=True)
    pdss = models.CharField(max_length=1, blank=True, null=True)
    estatus = models.CharField(max_length=50, blank=True, null=True)
    enviar = models.CharField(max_length=1, blank=True, null=True)
    integracion_laboratorio = models.CharField(max_length=1, blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    honorario = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    codigo_laboratorio = models.CharField(max_length=10, blank=True, null=True)
    internacional = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    exclusion_internacional = models.IntegerField(blank=True, null=True)
    simon = models.CharField(max_length=10, blank=True, null=True)
    codigo_integracion = models.CharField(max_length=10, blank=True, null=True)
    precio_us = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'estudio'


class EstudioKit(models.Model):
    estudiokitid = models.AutoField(primary_key=True)
    estudioid = models.IntegerField()
    productoid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'estudio_kit'


class EstudioLog(models.Model):
    logid = models.AutoField(primary_key=True)
    estudioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    costo_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudio_log'


class EstudioTipoPaciente(models.Model):
    estudioid = models.IntegerField(primary_key=True)
    tipopacienteid = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudio_tipo_paciente'
        unique_together = (('estudioid', 'tipopacienteid'),)


class EvolucionMedica(models.Model):
    evolucionid = models.AutoField(primary_key=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    enfermera = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()
    fecha_registro = models.DateTimeField(blank=True, null=True)
    hora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolucion_medica'


class Existencia(models.Model):
    existenciaid = models.AutoField(primary_key=True)
    productoid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2)
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'existencia'


class Factura(models.Model):
    facturaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    factura_paciente_tipo = models.CharField(max_length=3, blank=True, null=True)
    factura_paciente_numero = models.IntegerField(blank=True, null=True)
    fecha_reporte = models.DateTimeField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    glosa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    objecion_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    admisionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    operativoid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class FacturaCxp(models.Model):
    facturacxpid = models.AutoField(primary_key=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    facturaid = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    entradaid = models.IntegerField(blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_moneda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    itbis_moneda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento_moneda = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    informal = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    retencion_isr = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    retencion_itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    gravado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    exento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)
    propina = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    otros = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tiporetencionid = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    selectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    gravado_servicio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    exento_servicio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_cxp'


class FacturaCxpDetalle(models.Model):
    facturacxpid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    serviciogeneralid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo = models.IntegerField(blank=True, null=True)
    acuerdo_cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo_costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acuerdo_oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad_pendiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis_parte_costo = models.IntegerField()
    existencia_actual = models.DecimalField(max_digits=10, decimal_places=2)
    costo_actual = models.DecimalField(max_digits=18, decimal_places=2)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_cxp_detalle'
        unique_together = (('facturacxpid', 'detalleid'),)


class FacturaDetalle(models.Model):
    facturaid = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=3)
    detalleid = models.IntegerField()
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_detalle'
        unique_together = (('facturaid', 'tipo', 'detalleid'),)


class FacturaInt(models.Model):
    facturaintid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=3)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    fecha_entrada = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    causaid = models.IntegerField(blank=True, null=True)
    fecha_salida = models.DateTimeField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    poliza = models.CharField(max_length=20, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    ingresado = models.CharField(max_length=5, blank=True, null=True)
    referido = models.CharField(max_length=5, blank=True, null=True)
    alta = models.CharField(max_length=5, blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    resp_nombre = models.CharField(max_length=80, blank=True, null=True)
    resp_telefono = models.CharField(max_length=30, blank=True, null=True)
    resp_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    parentescoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    autorizacionid = models.IntegerField(blank=True, null=True)
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    resp_cedula = models.CharField(max_length=20, blank=True, null=True)
    certificadoid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    entregada = models.IntegerField(blank=True, null=True)
    usuarioid_entregada = models.IntegerField(blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    triaje_nivel = models.CharField(max_length=20, blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    cubiculo = models.CharField(max_length=10, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    hora_factura = models.DateTimeField(blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    cxc_seguroid = models.IntegerField(blank=True, null=True)
    cxc_pacienteid = models.IntegerField(blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    franquicia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    refacturacion_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cerrado = models.IntegerField()
    refacturacion = models.DecimalField(max_digits=18, decimal_places=2)
    refacturacion_subtotal = models.DecimalField(max_digits=18, decimal_places=2)
    refacturacion_descuento = models.DecimalField(max_digits=18, decimal_places=2)
    referidorid_hacia = models.IntegerField(blank=True, null=True)
    tarjeta_tasa = models.DecimalField(max_digits=10, decimal_places=2)
    tarjeta_monto = models.DecimalField(max_digits=18, decimal_places=2)
    refacturacion_fecha = models.DateTimeField(blank=True, null=True)
    pagado = models.DecimalField(max_digits=18, decimal_places=2)
    comision = models.DecimalField(max_digits=18, decimal_places=2)
    total_gastos = models.DecimalField(max_digits=18, decimal_places=2)
    comision_medico = models.DecimalField(max_digits=18, decimal_places=2)
    enviada = models.IntegerField()
    enviado_a = models.CharField(max_length=100, blank=True, null=True)
    recibido_de = models.CharField(max_length=100, blank=True, null=True)
    referido_de = models.CharField(max_length=100, blank=True, null=True)
    localidadid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_int'


class FacturaIntDetalle(models.Model):
    facturaintid = models.IntegerField()
    tipo = models.CharField(max_length=3)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factura_int_detalle'


class FacturaIntEstudio(models.Model):
    facturaintid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    codigo_seguro = models.CharField(max_length=10, blank=True, null=True)
    enviado_laboratorio = models.IntegerField(blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    laboratorioid = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    exclusion_internacional = models.IntegerField()
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_int_estudio'
        unique_together = (('facturaintid', 'detalleid'),)


class FacturaIntFormapago(models.Model):
    facturaintid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    formapagoid = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_int_formapago'
        unique_together = (('facturaintid', 'detalleid'),)


class FacturaIntHonorario(models.Model):
    facturainthonorarioid = models.AutoField(primary_key=True)
    facturaintid = models.ForeignKey(FacturaInt, models.DO_NOTHING, db_column='facturaintid')
    medicoid = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medicoid')
    monto = models.DecimalField(max_digits=18, decimal_places=2)
    fecha = models.DateTimeField()
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid')

    class Meta:
        managed = False
        db_table = 'factura_int_honorario'


class FacturaIntProducto(models.Model):
    facturaintid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_int_producto'
        unique_together = (('facturaintid', 'detalleid'),)


class FacturaProducto(models.Model):
    facturaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    turnoid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    empleadoid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2)
    razonid_descuento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_producto'


class FacturaProductoDetalle(models.Model):
    facturaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'factura_producto_detalle'
        unique_together = (('facturaid', 'detalleid'),)


class FacturaResumen(models.Model):
    facturaid = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=3)
    servicioid = models.IntegerField()
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_resumen'
        unique_together = (('facturaid', 'tipo', 'servicioid'),)


class FormaAdministracion(models.Model):
    formaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forma_administracion'


class FormaPagoGasto(models.Model):
    formapagoid = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    clave = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forma_pago_gasto'


class Formapago(models.Model):
    formapagoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    credito_empleado = models.IntegerField(blank=True, null=True)
    credito_cliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formapago'


class Frecuencia(models.Model):
    frecuenciaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    horas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frecuencia'


class GastoFinanciero(models.Model):
    gastoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    bancocuentaid = models.IntegerField(blank=True, null=True)
    cuenta_numero = models.CharField(max_length=30, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gasto_financiero'


class GastoFinancieroDetalle(models.Model):
    gastoid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    transaccionid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    referencia = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gasto_financiero_detalle'
        unique_together = (('gastoid', 'detalleid'),)


class GastoMenor(models.Model):
    gastoid = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha_ncf = models.DateTimeField(blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    transaccionid = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    propina = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gasto_menor'


class Glosa(models.Model):
    glosaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    ncf_modifica = models.CharField(max_length=20, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    conceptoid = models.IntegerField(blank=True, null=True)
    generancf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glosa'


class GlosaDetalle(models.Model):
    glosaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    facturaid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'glosa_detalle'
        unique_together = (('glosaid', 'detalleid'),)


class Habitacion(models.Model):
    habitacionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    sectorid = models.IntegerField(blank=True, null=True)
    camas = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()
    quirofano = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'habitacion'


class HabitacionEstatus(models.Model):
    habestatusid = models.AutoField(primary_key=True)
    habitacionid = models.IntegerField()
    numero = models.CharField(max_length=15, blank=True, null=True)
    estatusid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'habitacion_estatus'


class HojaProductos(models.Model):
    servicioid = models.IntegerField(primary_key=True)
    productoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hoja_productos'
        unique_together = (('servicioid', 'productoid'),)


class Honorario(models.Model):
    honorarioid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total_facturado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'honorario'


class HonorarioDetalle(models.Model):
    honorarioid = models.IntegerField(primary_key=True)
    dethonorarioid = models.IntegerField()
    detalleid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    facturado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    total_factura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'honorario_detalle'
        unique_together = (('honorarioid', 'dethonorarioid'),)


class HonorariosConfig(models.Model):
    honorariosid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobrar = models.IntegerField(blank=True, null=True)
    asegurado_privado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'honorarios_config'


class ImagenesCola(models.Model):
    colaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    hora_solicitud = models.DateTimeField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    fecha_realizado = models.DateTimeField(blank=True, null=True)
    hora_realizado = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes_cola'


class InformeConfig(models.Model):
    servicioid = models.IntegerField(primary_key=True)
    especialidadid = models.IntegerField()
    valida = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informe_config'
        unique_together = (('servicioid', 'especialidadid'),)


class InformeVario(models.Model):
    informeid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informe_vario'


class Informerx(models.Model):
    informeid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informerx'


class IntegracionLaboratorioSecuencia(models.Model):
    laboratorioid = models.AutoField(primary_key=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integracion_laboratorio_secuencia'


class IntegracionLaboratorioSecuencia1(models.Model):
    laboratorioid = models.IntegerField()
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'integracion_laboratorio_secuencia1'


class InventarioFisico(models.Model):
    fisicoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventario_fisico'


class InventarioFisicoDetalle(models.Model):
    fisicoid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    cod_barra = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    contado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    existencia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    controlado = models.CharField(max_length=1, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_fisico_detalle'
        unique_together = (('fisicoid', 'detalleid'),)


class Itbis(models.Model):
    itbisid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    porciento = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'itbis'


class LabAntibiograma(models.Model):
    antibiogramaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_antibiograma'


class LabAntibiogramaDetalle(models.Model):
    antibiogramaid = models.IntegerField(primary_key=True)
    antibioticoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lab_antibiograma_detalle'
        unique_together = (('antibiogramaid', 'antibioticoid'),)


class LabAntibiotico(models.Model):
    antibioticoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    predeterminadoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_antibiotico'


class LabBateria(models.Model):
    bacteriaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=10, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_bateria'


class LabCola(models.Model):
    colaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    hora_solicitud = models.DateTimeField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    fecha_realizado = models.DateTimeField(blank=True, null=True)
    hora_realizado = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_cola'


class LabGrupo(models.Model):
    labgrupoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_grupo'


class LabMedida(models.Model):
    labmedidaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_medida'


class LabMetodo(models.Model):
    metodoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_metodo'


class LabParametro(models.Model):
    estudioid = models.IntegerField()
    parametroid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)
    capacidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    predeterminadoid = models.IntegerField(blank=True, null=True)
    metodoid = models.IntegerField(blank=True, null=True)
    equipoid = models.IntegerField(blank=True, null=True)
    tipovariable = models.CharField(max_length=1, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    labgrupoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_parametro'


class LabParametroLista(models.Model):
    listaid = models.AutoField(primary_key=True)
    parametroid = models.IntegerField(blank=True, null=True)
    predeterminadoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_parametro_lista'


class LabPredeterminado(models.Model):
    predeterminadoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_predeterminado'


class LabRequisito(models.Model):
    requisitoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_requisito'


class LabResultado(models.Model):
    resultadoid = models.AutoField(primary_key=True)
    fecha_factura = models.DateTimeField(blank=True, null=True)
    hora_factura = models.DateTimeField(blank=True, null=True)
    fecha_reporte = models.DateTimeField(blank=True, null=True)
    hora_reporte = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    laboratorioid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    entregado = models.IntegerField(blank=True, null=True)
    enviado = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_resultado'


class LabResultadoDetalle(models.Model):
    resultadoid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    parametroid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    resultado = models.CharField(max_length=100, blank=True, null=True)
    labmedidaid = models.IntegerField(blank=True, null=True)
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    metodoid = models.IntegerField(blank=True, null=True)
    abreviatura = models.CharField(max_length=10, blank=True, null=True)
    labgrupoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_resultado_detalle'
        unique_together = (('resultadoid', 'detalleid'),)


class LabSeccion(models.Model):
    seccionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_seccion'


class LabTipoenvase(models.Model):
    tipoenvaseid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_tipoenvase'


class LabTipomuestra(models.Model):
    tipomuestraid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    etiquetas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_tipomuestra'


class Localidad(models.Model):
    localidadid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidad'


class Mamografia(models.Model):
    mamografiaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mamografia'


class Medico(models.Model):
    medicoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    beeper = models.CharField(max_length=30, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    planta = models.IntegerField(blank=True, null=True)
    execuatur = models.CharField(max_length=20, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    consulta_medica = models.IntegerField(blank=True, null=True)
    recetario_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    personal_correo = models.CharField(max_length=100, blank=True, null=True)
    personal_telefono = models.CharField(max_length=20, blank=True, null=True)
    personal_celular = models.CharField(max_length=20, blank=True, null=True)
    personal_direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    opc = models.IntegerField(blank=True, null=True)
    fecha_nac = models.DateTimeField(blank=True, null=True)
    google_id = models.CharField(max_length=50, blank=True, null=True)
    google_password = models.CharField(max_length=50, blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    internacional_fondo_comun = models.DecimalField(max_digits=10, decimal_places=2)
    internacional_fondo_comun_grupo = models.CharField(max_length=5, blank=True, null=True)
    internacional_porc_honorario = models.DecimalField(max_digits=10, decimal_places=2)
    consultorio_numero = models.CharField(max_length=10, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class MedicoCalendarioCita(models.Model):
    calendariocitaid = models.AutoField(primary_key=True)
    medicoid = models.ForeignKey(Medico, models.DO_NOTHING, db_column='medicoid')
    fecha = models.DateTimeField()
    hora = models.DateTimeField()
    disponible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medico_calendario_cita'


class MedicoFoto(models.Model):
    medicoid = models.IntegerField(blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    fotoid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico_foto'


class Medida(models.Model):
    medidaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medida'


class Moneda(models.Model):
    monedaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    simbolo = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneda'


class NcfPerdido(models.Model):
    ncfperdidoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ncf_perdido'


class NcfTipo(models.Model):
    tiponcfid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    identificacion = models.CharField(max_length=11, blank=True, null=True)
    secuencia_desde = models.IntegerField(blank=True, null=True)
    secuencia_hasta = models.IntegerField(blank=True, null=True)
    secuencia_actual = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    stop = models.CharField(max_length=1, blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'ncf_tipo'


class Nomina(models.Model):
    nominaid = models.AutoField(primary_key=True)
    tipoid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_nomina = models.DateTimeField(blank=True, null=True)
    cant_mensual = models.IntegerField(blank=True, null=True)
    total_ingresos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    total_descuentos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cant_empleados = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina'


class NominaCalendarioFiesta(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_calendario_fiesta'


class NominaCarta(models.Model):
    cartaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_carta'


class NominaCartaCampo(models.Model):
    cartaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    valor = models.CharField(max_length=100, blank=True, null=True)
    campo = models.CharField(max_length=100, blank=True, null=True)
    funcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_carta_campo'
        unique_together = (('cartaid', 'detalleid'),)


class NominaConfigImpresion(models.Model):
    configid = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    secuencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_config_impresion'


class NominaConfigReporte(models.Model):
    configid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_config_reporte'


class NominaConfigReporteDetalle(models.Model):
    configid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_config_reporte_detalle'
        unique_together = (('configid', 'detalleid'),)


class NominaDetalle(models.Model):
    nominaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    empleadoid = models.IntegerField(blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    tipoingresoid = models.IntegerField(blank=True, null=True)
    tipodescuentoid = models.IntegerField(blank=True, null=True)
    ing_nombre = models.CharField(max_length=20, blank=True, null=True)
    des_nombre = models.CharField(max_length=20, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    cargoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    aporte = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nota = models.CharField(max_length=100, blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    banco_cuenta_tipo = models.CharField(max_length=1, blank=True, null=True)
    forma_pago = models.CharField(max_length=1, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    dias = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_detalle'
        unique_together = (('nominaid', 'detalleid'),)


class NominaIsr(models.Model):
    isrid = models.AutoField(primary_key=True)
    desde = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    hasta = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porciento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    exceso_monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_isr'


class NominaMotivo(models.Model):
    motivoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_motivo'


class NominaPrestaciones(models.Model):
    prestacionid = models.AutoField(primary_key=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)
    salario_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_mensual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_diario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    preavisado = models.IntegerField(blank=True, null=True)
    cesantia = models.IntegerField(blank=True, null=True)
    vacaciones = models.IntegerField(blank=True, null=True)
    navidad = models.IntegerField(blank=True, null=True)
    salario_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_4 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_5 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_6 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_7 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_8 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_9 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_10 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_11 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    salario_12 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_3 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_4 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_5 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_6 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_7 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_8 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_9 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_10 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_11 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_12 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_preaviso = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_cesantia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_vacacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_navidad = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_prestaciones'


class NominaTipo(models.Model):
    tipoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    cant_mensual = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    banco_cuenta = models.CharField(max_length=50, blank=True, null=True)
    archivo = models.CharField(max_length=100, blank=True, null=True)
    ruta = models.IntegerField(blank=True, null=True)
    banco_codigo = models.IntegerField(blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    genera_asiento = models.IntegerField(blank=True, null=True)
    porc_hora_extra = models.DecimalField(max_digits=10, decimal_places=2)
    porc_hora_feriado = models.DecimalField(max_digits=10, decimal_places=2)
    porc_hora_nocturna = models.DecimalField(max_digits=10, decimal_places=2)
    porc_hora_vacaciones = models.DecimalField(max_digits=10, decimal_places=2)
    porc_hora_licencia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'nomina_tipo'


class NominaTipoDescuento(models.Model):
    tipodescuentoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuentaid = models.CharField(max_length=20, blank=True, null=True)
    aporte_empresa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aporte_empleado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salario_tope = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nombre_reporte = models.CharField(max_length=20, blank=True, null=True)
    periodo = models.CharField(max_length=1, blank=True, null=True)
    ley = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_tipo_descuento'


class NominaTipoIngreso(models.Model):
    tipoingresoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuentaid = models.CharField(max_length=20, blank=True, null=True)
    calcula_liq = models.CharField(max_length=5, blank=True, null=True)
    calcula_isr = models.CharField(max_length=5, blank=True, null=True)
    calcula_regalia = models.CharField(max_length=5, blank=True, null=True)
    nombre_reporte = models.CharField(max_length=20, blank=True, null=True)
    calcula_sfs = models.CharField(max_length=5, blank=True, null=True)
    calcula_afp = models.CharField(max_length=5, blank=True, null=True)
    periodo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_tipo_ingreso'


class Notacredito(models.Model):
    notacreditoid = models.AutoField(primary_key=True)
    clienteid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ncf_modifica = models.CharField(max_length=20, blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    cafeteriaid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    notadebitoid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    razonid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notacredito'


class NotacreditoCxp(models.Model):
    notacxpid = models.AutoField(primary_key=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    facturacxpid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ncf_modifica = models.CharField(max_length=20, blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    facturaid = models.CharField(max_length=20, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notacredito_cxp'


class Notadebito(models.Model):
    notadebitoid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    vence = models.DateTimeField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'notadebito'


class NotadebitoCxp(models.Model):
    notadebitocxpid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    vence = models.DateTimeField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=19, blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    ncf_modifica = models.CharField(max_length=19, blank=True, null=True)
    facturacxpid = models.IntegerField(blank=True, null=True)
    facturaid = models.CharField(max_length=20, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monto_bien = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto_servicio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'notadebito_cxp'


class Opc(models.Model):
    opcid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clave = models.CharField(max_length=6, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    generancf = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opc'


class OpcFactura(models.Model):
    opcfacturaid = models.AutoField(primary_key=True)
    opcid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    poliza = models.CharField(max_length=10, blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_gastos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    almacenid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    refacturacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_medico = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    referidorid_hacia = models.IntegerField(blank=True, null=True)
    franquicia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    formapagoid_franquicia = models.IntegerField(blank=True, null=True)
    refacturacion_fecha = models.DateTimeField(blank=True, null=True)
    cxc_seguroid = models.IntegerField(blank=True, null=True)
    cxc_pacienteid = models.IntegerField(blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    fecha_atencion = models.DateTimeField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    habitacion = models.CharField(max_length=20, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=100, blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    razonid = models.IntegerField(blank=True, null=True)
    cerrado = models.IntegerField(blank=True, null=True)
    usuarioid_cerrado = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    refacturacion_subtotal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    refacturacion_descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    refacturacion_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta_tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    enviada = models.IntegerField(blank=True, null=True)
    operativoid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    localidadid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opc_factura'


class OpcFacturaEstudio(models.Model):
    opcfacturaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opc_factura_estudio'
        unique_together = (('opcfacturaid', 'detalleid'),)


class OpcFacturaFormapago(models.Model):
    opcfacturaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    formapagoid = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opc_factura_formapago'
        unique_together = (('opcfacturaid', 'detalleid'),)


class OpcFacturaProducto(models.Model):
    opcfacturaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'opc_factura_producto'
        unique_together = (('opcfacturaid', 'detalleid'),)


class OpcRecibo(models.Model):
    opcreciboid = models.AutoField(primary_key=True)
    opc = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    formapagoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comision_medico = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    documento = models.CharField(max_length=20, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    refacturacion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_gastos = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    porc_comision_medico = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    razonid = models.IntegerField(blank=True, null=True)
    porc_comision_original = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porc_comision_medico_original = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    porc_comision = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aplica_rd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opc_recibo'


class Operativo(models.Model):
    operativoid = models.AutoField(primary_key=True)
    clienteid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operativo'


class Orden(models.Model):
    ordenid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pagada = models.CharField(max_length=5, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    facturada = models.CharField(max_length=1, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    auditoria = models.IntegerField(blank=True, null=True)
    auditoria_fecha = models.DateTimeField(blank=True, null=True)
    auditoria_usuario = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    auditoria_nota = models.CharField(max_length=2000, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    glosa = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    packid = models.IntegerField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    autorizacion_linea = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    recetaid = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    entregada = models.IntegerField(blank=True, null=True)
    usuarioid_entregada = models.IntegerField(blank=True, null=True)
    seguro_pagada = models.IntegerField(blank=True, null=True)
    seguro_pagada_fecha = models.DateTimeField(blank=True, null=True)
    operativoid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    referidorid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    auditoria_nota_medica = models.CharField(max_length=2000, blank=True, null=True)
    honorarioid = models.IntegerField(blank=True, null=True)
    estatusid = models.IntegerField(blank=True, null=True)
    tipoglosaid = models.IntegerField(blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota_concurrencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    detalle_incidencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipoincidenciaid = models.IntegerField(blank=True, null=True)
    auditoria_glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf_fecha_vence = models.DateTimeField(blank=True, null=True)
    pre_empleo = models.IntegerField(blank=True, null=True)
    facturaintid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    servicio_integracion_usuario = models.CharField(max_length=20, blank=True, null=True)
    servicio_integracion_clave = models.CharField(max_length=10, blank=True, null=True)
    usuarioid_cobertura_disponible = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden'


class OrdenCampos(models.Model):
    ordencampoid = models.AutoField(primary_key=True)
    ordenid = models.IntegerField(blank=True, null=True)
    campo = models.CharField(max_length=50, blank=True, null=True)
    valor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_campos'


class OrdenEstudio(models.Model):
    ordenid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_seguro = models.CharField(max_length=10, blank=True, null=True)
    enviado_laboratorio = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    cobrar_honorario = models.IntegerField(blank=True, null=True)
    informeid = models.IntegerField(blank=True, null=True)
    integracion_laboratorio = models.CharField(max_length=1, blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monto_honorario = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    total_cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    usuarioid_inserta = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    usuarioid_elimina = models.IntegerField(blank=True, null=True)
    fecha_inserta = models.DateTimeField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    fecha_elimina = models.DateTimeField(blank=True, null=True)
    exclusion_internacional = models.IntegerField(blank=True, null=True)
    simon = models.CharField(max_length=10, blank=True, null=True)
    actualiza_tarifario = models.IntegerField()
    descuento = models.DecimalField(max_digits=18, decimal_places=2)
    razonid_descuento = models.IntegerField(blank=True, null=True)
    descuento_temporada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orden_estudio'
        unique_together = (('ordenid', 'detalleid'),)


class OrdenFirma(models.Model):
    ordenfirmaid = models.AutoField(primary_key=True)
    ordenid = models.IntegerField()
    tipo = models.CharField(max_length=1)
    firma = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_firma'


class OrdenHonorario(models.Model):
    ordenid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    medicoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobrar = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_honorario'
        unique_together = (('ordenid', 'detalleid'),)


class OrdenLog(models.Model):
    logid = models.AutoField(primary_key=True)
    ordenid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nota = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_log'


class OrdenMedica(models.Model):
    ordenmedicaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    productoid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    prioridad = models.CharField(max_length=1, blank=True, null=True)
    realizada = models.IntegerField(blank=True, null=True)
    fecha_realizada = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    justificacion = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    medidaid_dosis = models.IntegerField(blank=True, null=True)
    cantidad_requisicion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    despachada = models.IntegerField(blank=True, null=True)
    fecha_despachada = models.DateTimeField(blank=True, null=True)
    hora_administracion = models.DateTimeField(blank=True, null=True)
    administrada = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()
    fecha_registro = models.DateTimeField(blank=True, null=True)
    hora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_medica'


class OrdenProducto(models.Model):
    ordenid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    total_cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orden_producto'
        unique_together = (('ordenid', 'detalleid'),)


class Orden_medica(models.Model):
    ordenmedicaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    dieta = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ordenmedica'


class OrdenmedicaDetalle(models.Model):
    ordenmedicaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    realizada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    despachada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_aministra = models.DateTimeField(blank=True, null=True)
    hora_administra = models.DateTimeField(blank=True, null=True)
    urgente = models.IntegerField(blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    requisicionid = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cups = models.CharField(max_length=10, blank=True, null=True)
    cubierto = models.IntegerField(blank=True, null=True)
    cantidad_requisicion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    medicoid_cirujano = models.IntegerField(blank=True, null=True)
    medicoid_anestesia = models.IntegerField(blank=True, null=True)
    medicoid_ayudante = models.IntegerField(blank=True, null=True)
    quirurgico_fecha = models.DateTimeField(blank=True, null=True)
    quirurgico_descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    quirurgico = models.CharField(max_length=1, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    exclusion_internacional = models.IntegerField(blank=True, null=True)
    validar_informe = models.IntegerField()
    simon = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenmedica_detalle'
        unique_together = (('ordenmedicaid', 'detalleid'),)


class Paciente(models.Model):
    pacienteid = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    estadocivilid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    profesionid = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_fellecio = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    motivo_fellecio = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    foto = models.CharField(max_length=100, blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=13, blank=True, null=True)
    pasaporte = models.CharField(max_length=20, blank=True, null=True)
    apodo = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipopacienteid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    web_usuario = models.CharField(max_length=50, blank=True, null=True)
    web_clave = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacunas = models.TextField(blank=True, null=True)  # This field type is a guess.
    antecedentes = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento = models.TextField(blank=True, null=True)  # This field type is a guess.
    cirugias = models.TextField(blank=True, null=True)  # This field type is a guess.
    cronicas = models.TextField(blank=True, null=True)  # This field type is a guess.
    habitos_personales = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    trabajo_telefono = models.CharField(max_length=20, blank=True, null=True)
    trabajo_nombre = models.CharField(max_length=100, blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    antecedentes_familiares = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_grato = models.IntegerField(blank=True, null=True)
    vip_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    nograto_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    gestion_cobro = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    codigo_anterior = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Paciente1(models.Model):
    pacienteid = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    estadocivilid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    profesionid = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_fellecio = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    motivo_fellecio = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    foto = models.CharField(max_length=100, blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=13, blank=True, null=True)
    pasaporte = models.CharField(max_length=20, blank=True, null=True)
    apodo = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipopacienteid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    web_usuario = models.CharField(max_length=50, blank=True, null=True)
    web_clave = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacunas = models.TextField(blank=True, null=True)  # This field type is a guess.
    antecedentes = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento = models.TextField(blank=True, null=True)  # This field type is a guess.
    cirugias = models.TextField(blank=True, null=True)  # This field type is a guess.
    cronicas = models.TextField(blank=True, null=True)  # This field type is a guess.
    habitos_personales = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    trabajo_telefono = models.CharField(max_length=20, blank=True, null=True)
    trabajo_nombre = models.CharField(max_length=100, blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    antecedentes_familiares = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_grato = models.IntegerField(blank=True, null=True)
    vip_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    nograto_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    gestion_cobro = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente1'


class PacienteAlergia(models.Model):
    pacientealergiaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    nombre = models.CharField(max_length=100)
    ano_diagnosis = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3)
    ocasionado_por = models.CharField(max_length=100, blank=True, null=True)
    reaccion = models.CharField(max_length=100, blank=True, null=True)
    cuando_ocurre = models.CharField(max_length=100, blank=True, null=True)
    medico = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicandose = models.IntegerField()
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_alergia'


class PacienteArchivo(models.Model):
    archivoid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    tipoarchivoid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ruta = models.CharField(max_length=2000, blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    facturaintid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_archivo'


class PacienteCirugia(models.Model):
    pacientecirugiaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    nombre = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    medico = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_cirugia'


class PacienteEnfermedad(models.Model):
    enfermedadpacienteid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    nombre = models.CharField(max_length=100)
    ano_diagnosis = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3)
    medico = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicandose = models.IntegerField()
    usuarioid = models.IntegerField(blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_enfermedad'


class PacienteFamilia(models.Model):
    pacientefamiliaid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    parentescoid = models.IntegerField()
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_familia'


class PacienteHospitalizacion(models.Model):
    hospitalizacionid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    hospital = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    seguro = models.CharField(max_length=100, blank=True, null=True)
    razon = models.CharField(max_length=100, blank=True, null=True)
    cie10 = models.CharField(max_length=10, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_hospitalizacion'


class PacienteMedicacion(models.Model):
    pacienteproductoid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField()
    productoid = models.IntegerField()
    viaid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    presentacionid = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.DecimalField(max_digits=18, decimal_places=2)
    momento = models.CharField(max_length=50, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    medico = models.CharField(max_length=100, blank=True, null=True)
    efectos_secundarios = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_medicacion'


class PacientePunto(models.Model):
    puntoid = models.AutoField(primary_key=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_punto'


class Pacientes(models.Model):
    pacienteid = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    estadocivilid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    profesionid = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_fellecio = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    motivo_fellecio = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    foto = models.CharField(max_length=100, blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=13, blank=True, null=True)
    pasaporte = models.CharField(max_length=20, blank=True, null=True)
    apodo = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipopacienteid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    web_usuario = models.CharField(max_length=50, blank=True, null=True)
    web_clave = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacunas = models.TextField(blank=True, null=True)  # This field type is a guess.
    antecedentes = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento = models.TextField(blank=True, null=True)  # This field type is a guess.
    cirugias = models.TextField(blank=True, null=True)  # This field type is a guess.
    cronicas = models.TextField(blank=True, null=True)  # This field type is a guess.
    habitos_personales = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    trabajo_telefono = models.CharField(max_length=20, blank=True, null=True)
    trabajo_nombre = models.CharField(max_length=100, blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    antecedentes_familiares = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_grato = models.IntegerField(blank=True, null=True)
    vip_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    nograto_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    gestion_cobro = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes'


class Pack(models.Model):
    packid = models.AutoField(primary_key=True)
    servicioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pre_empleo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pack'


class PackDetalle(models.Model):
    packid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pack_detalle'
        unique_together = (('packid', 'detalleid'),)


class PackEmergencia(models.Model):
    packid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pack_emergencia'


class PackEmergenciaDetalle(models.Model):
    packid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pack_emergencia_detalle'
        unique_together = (('packid', 'detalleid'),)


class PackProducto(models.Model):
    packid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pack_producto'
        unique_together = (('packid', 'detalleid'),)


class Padron(models.Model):
    seq_ced = models.CharField(max_length=10, blank=True, null=True)
    mun_ced = models.CharField(max_length=4, blank=True, null=True)
    ver_ced = models.CharField(max_length=2, blank=True, null=True)
    nombre1 = models.CharField(max_length=30, blank=True, null=True)
    nombre2 = models.CharField(max_length=30, blank=True, null=True)
    apellido1 = models.CharField(max_length=30, blank=True, null=True)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    fechanac = models.DateTimeField(blank=True, null=True)
    calle = models.CharField(max_length=40, blank=True, null=True)
    casa = models.CharField(max_length=5, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    edificio = models.CharField(max_length=40, blank=True, null=True)
    piso = models.CharField(max_length=10, blank=True, null=True)
    apto = models.CharField(max_length=10, blank=True, null=True)
    cod_mun = models.CharField(max_length=3, blank=True, null=True)
    cod_ciudad = models.CharField(max_length=2, blank=True, null=True)
    cod_sector = models.CharField(max_length=4, blank=True, null=True)
    pasaporte = models.CharField(max_length=12, blank=True, null=True)
    residencia = models.CharField(max_length=12, blank=True, null=True)
    lugarnac = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'padron'


class Pais(models.Model):
    paisid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Parametros(models.Model):
    parametroid = models.AutoField(primary_key=True)
    servicioid_emer = models.IntegerField(blank=True, null=True)
    tipo_admision_normal = models.IntegerField(blank=True, null=True)
    nota_admision = models.TextField(blank=True, null=True)  # This field type is a guess.
    rol_cajero = models.IntegerField(blank=True, null=True)
    ed_internamiento = models.IntegerField(blank=True, null=True)
    ed_emergencia = models.IntegerField(blank=True, null=True)
    ed_ambulatorio = models.IntegerField(blank=True, null=True)
    ed_recibo = models.IntegerField(blank=True, null=True)
    ed_desembolso = models.IntegerField(blank=True, null=True)
    ed_entrada = models.IntegerField(blank=True, null=True)
    ed_despacho = models.IntegerField(blank=True, null=True)
    ed_devolucion = models.IntegerField(blank=True, null=True)
    cta_cobertura = models.CharField(max_length=15, blank=True, null=True)
    cta_descuento = models.CharField(max_length=15, blank=True, null=True)
    cta_paciente = models.CharField(max_length=15, blank=True, null=True)
    servicioid_honorarios = models.IntegerField(blank=True, null=True)
    cta_honorario = models.CharField(max_length=50, blank=True, null=True)
    cta_inventario = models.CharField(max_length=15, blank=True, null=True)
    cta_costo = models.CharField(max_length=15, blank=True, null=True)
    formato_recibo = models.CharField(max_length=1, blank=True, null=True)
    formato_ambularorio = models.CharField(max_length=1, blank=True, null=True)
    formato_desembolso = models.CharField(max_length=1, blank=True, null=True)
    tiponcf_consumidor = models.IntegerField(blank=True, null=True)
    tiponcf_valorfiscal = models.IntegerField(blank=True, null=True)
    rol_medico = models.IntegerField(blank=True, null=True)
    rol_auditor = models.IntegerField(blank=True, null=True)
    servicioid_rx = models.IntegerField(blank=True, null=True)
    especialidadid_rx = models.IntegerField(blank=True, null=True)
    timbrado_rx = models.IntegerField(blank=True, null=True)
    timbrado_aut_alta = models.IntegerField(blank=True, null=True)
    servicioid_medicamento = models.IntegerField(blank=True, null=True)
    rol_enfermera = models.IntegerField(blank=True, null=True)
    servicioid_sonografia = models.IntegerField(blank=True, null=True)
    especialidadid_sonografia = models.IntegerField(blank=True, null=True)
    laboratorio_integracion = models.CharField(max_length=20, blank=True, null=True)
    laboratorio_integracion_db = models.CharField(max_length=200, blank=True, null=True)
    servicioid_laboratorio = models.IntegerField(blank=True, null=True)
    laboratorio_integracion_tabla = models.CharField(max_length=50, blank=True, null=True)
    servicioid_endoscopia = models.IntegerField(blank=True, null=True)
    especialidadid_gastro = models.IntegerField(blank=True, null=True)
    timbrado_sonografia = models.IntegerField(blank=True, null=True)
    timbrado_endoscopia = models.IntegerField(blank=True, null=True)
    servicioid_materialgastable = models.IntegerField(blank=True, null=True)
    autoriza_emergencia = models.IntegerField(blank=True, null=True)
    autoriza_admision = models.IntegerField(blank=True, null=True)
    servicioid_cirugia = models.IntegerField(blank=True, null=True)
    cta_caja = models.CharField(max_length=15, blank=True, null=True)
    tiponcf_notacredito = models.IntegerField(blank=True, null=True)
    servicioid_tomografia = models.IntegerField(blank=True, null=True)
    servicioid_mamografia = models.IntegerField(blank=True, null=True)
    timbrado_tomografia = models.IntegerField(blank=True, null=True)
    timbrado_mamografia = models.IntegerField(blank=True, null=True)
    nomina_descuento_isr = models.IntegerField(blank=True, null=True)
    nomina_ingreso_sueldo = models.IntegerField(blank=True, null=True)
    nomina_descuento_seguro = models.IntegerField(blank=True, null=True)
    nomina_descuento_prestamo = models.IntegerField(blank=True, null=True)
    nomina_dias_sueldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomina_precio_horas_extras = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_precio_horas_normales = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_precio_horas_fin_semana = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_precio_horas_feriados = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_precio_horas_nocturnas = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_horario_extra_desde = models.DateTimeField(blank=True, null=True)
    nomina_horario_extra_hasta = models.DateTimeField(blank=True, null=True)
    nomina_horario_nocturno_desde = models.DateTimeField(blank=True, null=True)
    nomina_horario_nocturno_hasta = models.DateTimeField(blank=True, null=True)
    nomina_horario_desde = models.DateTimeField(blank=True, null=True)
    nomina_horario_hasta = models.DateTimeField(blank=True, null=True)
    nomina_descanso_desde = models.DateTimeField(blank=True, null=True)
    nomina_descanso_hasta = models.DateTimeField(blank=True, null=True)
    nomina_ingreso_vacaciones = models.IntegerField(blank=True, null=True)
    ed_nomina = models.IntegerField(blank=True, null=True)
    cta_sueldo = models.CharField(max_length=15, blank=True, null=True)
    cta_regalia = models.CharField(max_length=15, blank=True, null=True)
    email_host = models.CharField(max_length=50, blank=True, null=True)
    email_user = models.CharField(max_length=50, blank=True, null=True)
    email_password = models.CharField(max_length=50, blank=True, null=True)
    email_port = models.IntegerField(blank=True, null=True)
    email_correo = models.CharField(max_length=50, blank=True, null=True)
    nomina_permisos_maximo = models.IntegerField(blank=True, null=True)
    causaid_parto = models.IntegerField(blank=True, null=True)
    nomina_descuento_sfs = models.IntegerField(blank=True, null=True)
    nomina_descuento_afp = models.IntegerField(blank=True, null=True)
    nomina_integracion_contable = models.CharField(max_length=1, blank=True, null=True)
    email_ssl = models.CharField(max_length=1, blank=True, null=True)
    usuarioid_cajero_nomina = models.IntegerField(blank=True, null=True)
    nomina_descuento_pos = models.IntegerField(blank=True, null=True)
    almacenid_pos = models.IntegerField(blank=True, null=True)
    servicioid_farmacia = models.IntegerField(blank=True, null=True)
    servicioid_doppler = models.IntegerField(blank=True, null=True)
    servicioid_ecocardiograma = models.IntegerField(blank=True, null=True)
    especialidadid_ecocardiografista = models.IntegerField(blank=True, null=True)
    ed_factura_seguro = models.IntegerField(blank=True, null=True)
    almacenid_principal = models.IntegerField(blank=True, null=True)
    formapago_efectivo = models.IntegerField(blank=True, null=True)
    formapago_tarjeta = models.IntegerField(blank=True, null=True)
    rolid_admin = models.IntegerField(blank=True, null=True)
    nota_pos1 = models.CharField(max_length=80, blank=True, null=True)
    nota_pos2 = models.CharField(max_length=80, blank=True, null=True)
    nota_pos3 = models.CharField(max_length=80, blank=True, null=True)
    nota_pos4 = models.CharField(max_length=80, blank=True, null=True)
    nota_pos5 = models.CharField(max_length=80, blank=True, null=True)
    nomina_dias_vacaciones = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomina_cant_dias_vac_1 = models.IntegerField(blank=True, null=True)
    nomina_cant_dias_vac_2 = models.IntegerField(blank=True, null=True)
    pos_nombre = models.CharField(max_length=100, blank=True, null=True)
    pos_direccion1 = models.CharField(max_length=100, blank=True, null=True)
    pos_direccion2 = models.CharField(max_length=100, blank=True, null=True)
    pos_telefono = models.CharField(max_length=100, blank=True, null=True)
    seguroid_universal = models.IntegerField(blank=True, null=True)
    url_autorizador = models.CharField(max_length=100, blank=True, null=True)
    servicioid_consultas = models.IntegerField(blank=True, null=True)
    cta_cxc_empleado = models.CharField(max_length=15, blank=True, null=True)
    cta_itbis = models.CharField(max_length=15, blank=True, null=True)
    informes_sello_firma = models.IntegerField(blank=True, null=True)
    laboratorio_integracion_tipo = models.CharField(max_length=1, blank=True, null=True)
    tiponcf_proveedorinformal = models.IntegerField(blank=True, null=True)
    cta_descuento_compra = models.CharField(max_length=15, blank=True, null=True)
    receta_vencimiento = models.IntegerField(blank=True, null=True)
    seguroid_palic = models.IntegerField(blank=True, null=True)
    url_autorizador_palic = models.CharField(max_length=100, blank=True, null=True)
    barra = models.TextField(blank=True, null=True)  # This field type is a guess.
    emergencia_print_productos = models.IntegerField(blank=True, null=True)
    estudioid_emergencia = models.IntegerField(blank=True, null=True)
    almacenid_internamiento = models.IntegerField(blank=True, null=True)
    barra_triaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    triaje_impresora = models.CharField(max_length=50, blank=True, null=True)
    emergencia_interna = models.IntegerField(blank=True, null=True)
    cta_prima = models.CharField(max_length=15, blank=True, null=True)
    consulta_medica_dias = models.IntegerField(blank=True, null=True)
    dimensionid_cafeteria = models.IntegerField(blank=True, null=True)
    dimensionid_emergencia = models.IntegerField(blank=True, null=True)
    cta_itbis_compra = models.CharField(max_length=15, blank=True, null=True)
    cta_retencion_itbis = models.CharField(max_length=15, blank=True, null=True)
    cta_retencion_isr = models.CharField(max_length=15, blank=True, null=True)
    tiponcf_gastomenor = models.IntegerField(blank=True, null=True)
    estudioid_interconsulta_emergencia = models.IntegerField(blank=True, null=True)
    cta_resultado = models.CharField(max_length=15, blank=True, null=True)
    bancocuentaid_operaciones = models.IntegerField(blank=True, null=True)
    bancocuentaid_nomina = models.IntegerField(blank=True, null=True)
    cta_anticipo_cxp = models.CharField(max_length=15, blank=True, null=True)
    tiponcf_notadebito = models.IntegerField(blank=True, null=True)
    itbis = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    informeid_emergencia_admision = models.IntegerField(blank=True, null=True)
    emergencia_print_historia = models.IntegerField(blank=True, null=True)
    informeid_emergencia_alta = models.IntegerField(blank=True, null=True)
    triaje_modelo = models.CharField(max_length=1, blank=True, null=True)
    triaje_imprimir = models.IntegerField(blank=True, null=True)
    ruta_archivo_paciente = models.CharField(max_length=100, blank=True, null=True)
    nomina_ingreso_regalia = models.IntegerField(blank=True, null=True)
    emergencia_imprime_alta = models.IntegerField(blank=True, null=True)
    formato_factura_producto = models.CharField(max_length=1, blank=True, null=True)
    consulta_historia_sinfacturar = models.IntegerField(blank=True, null=True)
    estudioid_interconsulta_nocturna = models.IntegerField(blank=True, null=True)
    tope_rembolso_efectivo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    internconsulta_clave = models.IntegerField(blank=True, null=True)
    emergencia_hoja_egreso = models.IntegerField(blank=True, null=True)
    tipopacienteid_local = models.IntegerField(blank=True, null=True)
    honorarios_fuera = models.IntegerField(blank=True, null=True)
    itbis_parte_costo = models.IntegerField(blank=True, null=True)
    impresora_cheque = models.CharField(max_length=100, blank=True, null=True)
    url_interna = models.CharField(max_length=100, blank=True, null=True)
    internacional_gastos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    internacional_comision_imms = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seguroid_universal_solicita_medico = models.IntegerField(blank=True, null=True)
    url_rayosx = models.CharField(max_length=100, blank=True, null=True)
    internacional_comision_opc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    firma_paciente_admision = models.IntegerField(blank=True, null=True)
    firma_paciente_emergencia = models.IntegerField(blank=True, null=True)
    firma_paciente_ambulatorio = models.IntegerField(blank=True, null=True)
    firma_paciente_consulta = models.IntegerField(blank=True, null=True)
    internacional_comision_referidor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomina_dia_corte1 = models.IntegerField(blank=True, null=True)
    nomina_dia_corte2 = models.IntegerField(blank=True, null=True)
    nomina_credito_busqueda = models.CharField(max_length=1, blank=True, null=True)
    internacional_tipoclienteid_empresa = models.IntegerField(blank=True, null=True)
    internacional_tipoclienteid_empleado = models.IntegerField(blank=True, null=True)
    cta_propina = models.CharField(max_length=15, blank=True, null=True)
    triaje_impresora_internamiento = models.CharField(max_length=100, blank=True, null=True)
    admision_remite_paciente = models.IntegerField(blank=True, null=True)
    cta_resultado_anteriores = models.CharField(max_length=15, blank=True, null=True)
    tiponcf_notadebito_cxp = models.IntegerField(blank=True, null=True)
    emergencia_signos_vitales = models.IntegerField(blank=True, null=True)
    cta_ingreso_provisional = models.CharField(max_length=15, blank=True, null=True)
    estudioid_interconsulta_internamiento = models.IntegerField(blank=True, null=True)
    laboratorio_genera_sinpago = models.IntegerField(blank=True, null=True)
    url_medicamentos = models.CharField(max_length=100, blank=True, null=True)
    consulta_medica_pregunta = models.TextField(blank=True, null=True)  # This field type is a guess.
    consulta_medica_preguntar_seguridad = models.IntegerField(blank=True, null=True)
    rolid_tecnico = models.IntegerField(blank=True, null=True)
    despacho_varios_almacenes = models.IntegerField(blank=True, null=True)
    ncf_maximo_consumidorfinal = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    frequenciaid_unica = models.IntegerField(blank=True, null=True)
    emergencia_elimina_productos = models.IntegerField(blank=True, null=True)
    emergencia_modifica_productos = models.IntegerField(blank=True, null=True)
    emergencia_imprime_diagnostico = models.IntegerField(blank=True, null=True)
    cta_selectivo = models.CharField(max_length=15, blank=True, null=True)
    compra_periodo_stock = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    estudioid_honorario_internacional = models.IntegerField(blank=True, null=True)
    internacional_comision_imms2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    internacional_gastos2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    internacional_comision_referidor2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    internacional_comision_medico = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    emergencia_modifica_notas_medica = models.IntegerField(blank=True, null=True)
    admision_modifica_notas_medica = models.IntegerField(blank=True, null=True)
    emergencia_modifica_orden_medica = models.IntegerField(blank=True, null=True)
    admision_modifica_orden_medica = models.IntegerField(blank=True, null=True)
    servicioid_imagenes = models.IntegerField(blank=True, null=True)
    nomina_ingreso_horas_extras = models.IntegerField(blank=True, null=True)
    nomina_ingreso_horas_nocturnas = models.IntegerField(blank=True, null=True)
    nomina_ingreso_horas_feriado = models.IntegerField(blank=True, null=True)
    nomina_ingreso_horas_vacaciones = models.IntegerField(blank=True, null=True)
    nomina_ingreso_horas_licencia = models.IntegerField(blank=True, null=True)
    cuentaid_retencion_seguro = models.CharField(max_length=15, blank=True, null=True)
    producto_inactiva_existencia = models.IntegerField()
    inventario_factura_cxp = models.IntegerField()
    informes_imprime_fecha_reporte = models.IntegerField()
    titulo_honorario_fuera = models.CharField(max_length=200, blank=True, null=True)
    admision_servicios_orden = models.CharField(max_length=1)
    interfaz_firma = models.IntegerField()
    rembolso_paciente_tarjeta = models.IntegerField()
    ruta_archivo_empleado = models.CharField(max_length=100, blank=True, null=True)
    contabilidad_cierre_descuadrado = models.IntegerField()
    nomina_correo_volante = models.CharField(max_length=1)
    formato_consulta = models.CharField(max_length=1, blank=True, null=True)
    actualiza_tarifario = models.IntegerField()
    monedaid_local = models.IntegerField(blank=True, null=True)
    monedaid_usd = models.IntegerField(blank=True, null=True)
    nomina_descuento_percapita = models.IntegerField(blank=True, null=True)
    inventario_modifica_fecha = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parametros'


class ParametrosCamposOrden(models.Model):
    paramordenid = models.AutoField(primary_key=True)
    campo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametros_campos_orden'


class Parentesco(models.Model):
    parentescoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parentesco'


class PatronInforme(models.Model):
    patronid = models.AutoField(primary_key=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    detalle = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    internamiento = models.IntegerField(blank=True, null=True)
    imagen1 = models.BinaryField(blank=True, null=True)
    imagen2 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patron_informe'


class PatronMedicamento(models.Model):
    patronmedicamentoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3)
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    especialidadid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patron_medicamento'


class PatronMedicamentoDetalle(models.Model):
    patronmedicamentoid = models.IntegerField(primary_key=True)
    productoid = models.IntegerField()
    detalleid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    frecuenciaid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'patron_medicamento_detalle'
        unique_together = (('patronmedicamentoid', 'productoid', 'detalleid'),)


class Presentacion(models.Model):
    presentacionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presentacion'


class Presupuesto(models.Model):
    presupuestoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto'


class PresupuestoCuenta(models.Model):
    detalleid = models.AutoField(primary_key=True)
    presupuestoid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto_cuenta'


class PresupuestoDetalle(models.Model):
    detalleid = models.AutoField(primary_key=True)
    presupuestoid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presupuesto_detalle'


class Producto(models.Model):
    productoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    viaid = models.IntegerField(blank=True, null=True)
    presentacionid = models.IntegerField(blank=True, null=True)
    formaid = models.IntegerField(blank=True, null=True)
    tipoadministracionid = models.IntegerField(blank=True, null=True)
    tipoproductoid = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    controlado = models.CharField(max_length=1, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    existencia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vence = models.DateTimeField(blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cod_barra = models.CharField(max_length=20, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    medidaid = models.IntegerField(blank=True, null=True)
    alto_riesgo = models.CharField(max_length=1, blank=True, null=True)
    alto_riesgo_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    precio_cero = models.IntegerField(blank=True, null=True)
    itbis_venta = models.IntegerField()
    itbis_parte_costo = models.IntegerField()
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo_integracion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoLog(models.Model):
    logid = models.AutoField(primary_key=True)
    productoid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    costo_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    costo_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio_nuevo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_log'


class ProductoReorden(models.Model):
    productoid = models.IntegerField(primary_key=True)
    almacenid = models.IntegerField()
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_reorden'
        unique_together = (('productoid', 'almacenid'),)


class Profesion(models.Model):
    profesionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesion'


class Proveedor(models.Model):
    proveedorid = models.AutoField(primary_key=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=200, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    contacto_venta_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_venta_telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto_cobro_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_cobro_telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto_legal_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_legal_telefono = models.CharField(max_length=20, blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    limite = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    condicionid = models.IntegerField(blank=True, null=True)
    contacto_venta_correo = models.CharField(max_length=100, blank=True, null=True)
    contacto_cobro_correo = models.CharField(max_length=100, blank=True, null=True)
    contacto_legal_correo = models.CharField(max_length=100, blank=True, null=True)
    ban_cuenta_numero = models.CharField(max_length=20, blank=True, null=True)
    ban_cuenta_tipo = models.CharField(max_length=1, blank=True, null=True)
    ban_cuenta_codigo = models.CharField(max_length=10, blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    informal = models.IntegerField(blank=True, null=True)
    anticipo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bienid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class ProveedorAcuerdo(models.Model):
    acuerdoid = models.AutoField(primary_key=True)
    proveedorid = models.IntegerField()
    productoid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nota = models.CharField(max_length=200, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_acuerdo'


class Prueba(models.Model):
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba'


class Raza(models.Model):
    razaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raza'


class Razon(models.Model):
    razonid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    descuento = models.IntegerField()
    anula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'razon'


class Recibo(models.Model):
    reciboid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    rnc = models.CharField(max_length=11, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    ncf_nombre = models.CharField(max_length=200, blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cierreid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    admisionid_honorario = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)
    puntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibo'


class ReciboFactura(models.Model):
    reciboid = models.IntegerField(primary_key=True)
    facturaid = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_fecha = models.DateTimeField(blank=True, null=True)
    factura_vence = models.DateTimeField(blank=True, null=True)
    factura_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_pendiente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_int = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_amb = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_eme = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    glosa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    objecion_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    factura_cafeteria = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    factura_nd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_prod = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'recibo_factura'
        unique_together = (('reciboid', 'facturaid'),)


class ReciboFacturaDetalle(models.Model):
    reciboid = models.IntegerField(primary_key=True)
    facturaid = models.IntegerField()
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=50, blank=True, null=True)
    poliza = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    glosa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    pacienteid = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'recibo_factura_detalle'
        unique_together = (('reciboid', 'facturaid', 'detalleid'),)


class ReciboFormapago(models.Model):
    reciboid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    formapagoid = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    cheque = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    credito_empleado = models.IntegerField(blank=True, null=True)
    credito_cliente = models.IntegerField(blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibo_formapago'
        unique_together = (('reciboid', 'detalleid'),)


class Referidor(models.Model):
    referidorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referidor'


class Regalia(models.Model):
    regaliaid = models.AutoField(primary_key=True)
    fecha_regalia = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cant_empleados = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regalia'


class RegaliaDetalle(models.Model):
    regaliaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    empleadoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuenta = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    ingreso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    tiempo = models.IntegerField(blank=True, null=True)
    regalia = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    sueldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    banco_cuenta_tipo = models.CharField(max_length=1, blank=True, null=True)
    cargoid = models.IntegerField(blank=True, null=True)
    forma_pago = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regalia_detalle'
        unique_together = (('regaliaid', 'detalleid'),)


class Requisicion(models.Model):
    requisicionid = models.AutoField(primary_key=True)
    turnoid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    auditoriaid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    destino = models.CharField(max_length=1, blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    autorizada = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    comprada = models.IntegerField()
    uci = models.IntegerField()
    usuarioid_cierre = models.IntegerField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    nota_cierre = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'requisicion'


class RequisicionAutoriza(models.Model):
    requisicionid = models.IntegerField(primary_key=True)
    rolid = models.IntegerField()
    estatus = models.CharField(max_length=3, blank=True, null=True)
    fecha_autoriza = models.DateTimeField(blank=True, null=True)
    hora_autoriza = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_autoriza'
        unique_together = (('requisicionid', 'rolid'),)


class RequisicionCompra(models.Model):
    reqcompraid = models.AutoField(primary_key=True)
    requisicionid = models.ForeignKey(Requisicion, models.DO_NOTHING, db_column='requisicionid')
    compraid = models.ForeignKey(Compra, models.DO_NOTHING, db_column='compraid')

    class Meta:
        managed = False
        db_table = 'requisicion_compra'


class RequisicionDetalle(models.Model):
    requisicionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    dosis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidaid_dosis = models.IntegerField(blank=True, null=True)
    cantidad_pendiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad_orden = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    alto_riesgo = models.CharField(max_length=1, blank=True, null=True)
    cantidad_recibido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cod_barra = models.CharField(max_length=20, blank=True, null=True)
    req_automatica = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_detalle'
        unique_together = (('requisicionid', 'detalleid'),)


class RequisicionEstudio(models.Model):
    requisicionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    uci = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'requisicion_estudio'


class RequisicionEstudioDetalle(models.Model):
    requisicionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    estudioid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    codigo_seguro = models.CharField(max_length=10, blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_estudio_detalle'
        unique_together = (('requisicionid', 'detalleid'),)


class ReversoFactura(models.Model):
    reversointid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid')
    emergenciaid = models.ForeignKey(Emergencia, models.DO_NOTHING, db_column='emergenciaid', blank=True, null=True)
    admisionid = models.ForeignKey(Admision, models.DO_NOTHING, db_column='admisionid', blank=True, null=True)
    ordenid = models.ForeignKey(Orden, models.DO_NOTHING, db_column='ordenid', blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'reverso_factura'


class Rnc(models.Model):
    rnc_cedula = models.CharField(primary_key=True, max_length=30)
    razon_social = models.CharField(max_length=200, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=200, blank=True, null=True)
    actividad_economica = models.CharField(max_length=2000, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=200, blank=True, null=True)
    urbanizacion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    fecha_constitucion = models.CharField(max_length=200, blank=True, null=True)
    estatus = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rnc'


class Rol(models.Model):
    rolid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    autoriza = models.CharField(max_length=5, blank=True, null=True)
    codificar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class RolAccion(models.Model):
    rolinsertid = models.AutoField(primary_key=True)
    rolid = models.IntegerField()
    opcion_caption = models.CharField(max_length=100)
    opcion_name = models.CharField(max_length=100)
    inserta = models.IntegerField()
    modifica = models.IntegerField()
    elimina = models.IntegerField()
    seleccion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol_accion'


class RolAlmacen(models.Model):
    rolid = models.IntegerField(primary_key=True)
    almacenid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol_almacen'
        unique_together = (('rolid', 'almacenid'),)


class RolDepartamento(models.Model):
    rolid = models.IntegerField(primary_key=True)
    departamentoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol_departamento'
        unique_together = (('rolid', 'departamentoid'),)


class RolServicio(models.Model):
    rolid = models.IntegerField(primary_key=True)
    servicioid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rol_servicio'
        unique_together = (('rolid', 'servicioid'),)


class RrhhAccionPersonal(models.Model):
    accionid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    tipoid = models.IntegerField(blank=True, null=True)
    sueldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    concepto = models.CharField(max_length=100, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    departamentoid = models.IntegerField(blank=True, null=True)
    cargoid = models.IntegerField(blank=True, null=True)
    cargoid_actual = models.IntegerField(blank=True, null=True)
    departamentoid_actual = models.IntegerField(blank=True, null=True)
    sueldo_actual = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    estatus_actual = models.CharField(max_length=50, blank=True, null=True)
    estatus = models.CharField(max_length=50, blank=True, null=True)
    hora_desde = models.DateTimeField(blank=True, null=True)
    hora_hasta = models.DateTimeField(blank=True, null=True)
    motivoid = models.IntegerField(blank=True, null=True)
    fecha_desde = models.DateTimeField(blank=True, null=True)
    fecha_hasta = models.DateTimeField(blank=True, null=True)
    fecha_accion = models.DateTimeField(blank=True, null=True)
    accionid_reversa = models.IntegerField(blank=True, null=True)
    descontar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rrhh_accion_personal'


class RrhhAccionPersonalDetalle(models.Model):
    accionid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)
    dias = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rrhh_accion_personal_detalle'
        unique_together = (('accionid', 'detalleid'),)


class Salida(models.Model):
    salidaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    proveedorid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid = models.IntegerField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    tipo = models.CharField(max_length=1, blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salida'


class SalidaDetalle(models.Model):
    salidaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'salida_detalle'
        unique_together = (('salidaid', 'detalleid'),)


class Sangre(models.Model):
    sangreid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangre'


class Sector(models.Model):
    sectorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'


class Seguro(models.Model):
    seguroid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    rnc = models.CharField(max_length=11, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fax = models.CharField(max_length=30, blank=True, null=True)
    telefono_autorizacion = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=80, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    margen_medicamento = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    margen_material = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    repite_autorizacion = models.IntegerField(blank=True, null=True)
    codigo_prestador = models.CharField(max_length=50, blank=True, null=True)
    integracion_usuario = models.CharField(max_length=50, blank=True, null=True)
    integracion_pswd = models.CharField(max_length=50, blank=True, null=True)
    integracion_codigo = models.CharField(max_length=50, blank=True, null=True)
    contacto_cxp_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_cxp_telefono = models.CharField(max_length=50, blank=True, null=True)
    contacto_cxp_correo = models.CharField(max_length=50, blank=True, null=True)
    contacto_contratacion_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_contratacion_telefono = models.CharField(max_length=50, blank=True, null=True)
    contacto_contratacion_correo = models.CharField(max_length=50, blank=True, null=True)
    contacto_medica_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_medica_telefono = models.CharField(max_length=50, blank=True, null=True)
    contacto_medica_correo = models.CharField(max_length=50, blank=True, null=True)
    contacto_autoriz_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_autoriz_telefono = models.CharField(max_length=50, blank=True, null=True)
    contacto_autoriz_correo = models.CharField(max_length=50, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    nota_factura = models.TextField(blank=True, null=True)  # This field type is a guess.
    cobertura_emergencia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    solicita_info = models.IntegerField(blank=True, null=True)
    internacional = models.IntegerField(blank=True, null=True)
    cuentaid_opc = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_internacional = models.CharField(max_length=15, blank=True, null=True)
    ars_universal = models.IntegerField(blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)
    ars_palic = models.IntegerField()
    monedaid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seguro'


class SeguroPlan(models.Model):
    planid = models.AutoField(primary_key=True)
    seguroid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    nomina_precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nomina_porciento_empleado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nomina_porciento_dependiente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_plan'


class SeguroPrecio(models.Model):
    seguroid = models.IntegerField(primary_key=True)
    estudioid = models.IntegerField()
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    precio_us = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    simon = models.CharField(max_length=10, blank=True, null=True)
    cambiado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_precio'
        unique_together = (('seguroid', 'estudioid'),)


class SeguroPrecioEspecialidad(models.Model):
    seguroid = models.IntegerField(primary_key=True)
    estudioid = models.IntegerField()
    especialidadid = models.IntegerField()
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    simon = models.CharField(max_length=10, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    cambiado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_precio_especialidad'
        unique_together = (('seguroid', 'estudioid', 'especialidadid'),)


class SeguroPrecioHabitacion(models.Model):
    seguroid = models.IntegerField(primary_key=True)
    habitacionid = models.IntegerField()
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_precio_habitacion'
        unique_together = (('seguroid', 'habitacionid'),)


class SeguroPrecioMedico(models.Model):
    seguroid = models.IntegerField(primary_key=True)
    medicoid = models.IntegerField()
    codigo = models.CharField(max_length=10, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_precio_medico'
        unique_together = (('seguroid', 'medicoid'),)


class SeguroPrecioProducto(models.Model):
    seguroid = models.IntegerField(primary_key=True)
    productoid = models.IntegerField()
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cubierto_seguro = models.IntegerField(blank=True, null=True)
    cambiado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguro_precio_producto'
        unique_together = (('seguroid', 'productoid'),)


class Servicio(models.Model):
    servicioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    servicioidpadre = models.IntegerField(blank=True, null=True)
    inventario = models.CharField(max_length=5, blank=True, null=True)
    ambulatorio = models.CharField(max_length=5, blank=True, null=True)
    patron = models.CharField(max_length=1, blank=True, null=True)
    internamiento = models.CharField(max_length=5, blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cie10 = models.CharField(max_length=6, blank=True, null=True)
    cuentaid_costo = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_inventario = models.CharField(max_length=15, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    almacenid = models.IntegerField(blank=True, null=True)
    imprimir_claveweb = models.IntegerField(blank=True, null=True)
    especialidad = models.IntegerField(blank=True, null=True)
    ficha_paciente = models.IntegerField(blank=True, null=True)
    historia_clinica = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    consulta_medica = models.IntegerField(blank=True, null=True)
    informe_rx = models.IntegerField(blank=True, null=True)
    informe_sonografia = models.IntegerField(blank=True, null=True)
    informe_endoscopia = models.IntegerField(blank=True, null=True)
    informe_tomografia = models.IntegerField(blank=True, null=True)
    informe_mamografia = models.IntegerField(blank=True, null=True)
    informe_doppler = models.IntegerField(blank=True, null=True)
    informe_eco = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=5, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    hojas_ambulatorio = models.IntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=5, blank=True, null=True)
    cuentaid_descuento = models.CharField(max_length=15, blank=True, null=True)
    emergencia = models.IntegerField()
    integracion_web = models.IntegerField()
    validar_informe = models.IntegerField()
    tarifario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class ServicioCuenta(models.Model):
    serviciocuenta = models.AutoField(primary_key=True)
    servicioid = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    cuentaid_ing = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_cos = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_inv = models.CharField(max_length=15, blank=True, null=True)
    cuentaid_des = models.CharField(max_length=15, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_cuenta'


class ServicioEspecialidad(models.Model):
    servicioid = models.IntegerField(primary_key=True)
    especialidadid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio_especialidad'
        unique_together = (('servicioid', 'especialidadid'),)


class ServicioGeneral(models.Model):
    serviciogeneralid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cuentaid = models.CharField(max_length=15, blank=True, null=True)
    itbis = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_general'


class ServicioSeguro(models.Model):
    servicioid = models.IntegerField(primary_key=True)
    seguroid = models.IntegerField()
    codigo = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio_seguro'
        unique_together = (('servicioid', 'seguroid'),)


class Sexo(models.Model):
    sexoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sexo'


class SolicitudCompra(models.Model):
    solicitudid = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    sup_codigo = models.IntegerField(blank=True, null=True)
    concepto = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuarioid_solicita = models.IntegerField(blank=True, null=True)
    usuarioid_revisado = models.IntegerField(blank=True, null=True)
    usuarioid_aprueba = models.IntegerField(blank=True, null=True)
    fecha_revision = models.DateTimeField(blank=True, null=True)
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    compraid = models.IntegerField(blank=True, null=True)
    condicionid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    departamentoid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_compra'


class SolicitudCompraDetalle(models.Model):
    solicitudid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_compra_detalle'
        unique_together = (('solicitudid', 'detalleid'),)


class Sonografia(models.Model):
    sonografiaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sonografia'


class Sucursal(models.Model):
    sucursalid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion1 = models.CharField(max_length=100, blank=True, null=True)
    direccion2 = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    almacenid = models.IntegerField(blank=True, null=True)
    tiponcf_consumidor = models.IntegerField(blank=True, null=True)
    factura_con_seguro = models.IntegerField(blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dimensionid = models.IntegerField(blank=True, null=True)
    rnc = models.CharField(max_length=20, blank=True, null=True)
    consulta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class SucursalPrecio(models.Model):
    precioid = models.AutoField(primary_key=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    productoid = models.IntegerField(blank=True, null=True)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    minimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maximo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal_precio'


class Tarifa(models.Model):
    codigo = models.CharField(max_length=6, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    precio1 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio2 = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarifa'


class Tasa(models.Model):
    tasaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa_contable = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tasa_conversion = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasa'


class TipoAdmision(models.Model):
    tipoadmisionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_admision'


class TipoArchivo(models.Model):
    tipoarchivoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    paciente = models.IntegerField()
    empleado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_archivo'


class TipoAtencion(models.Model):
    tipoatencionid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    facturable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_atencion'


class TipoCliente(models.Model):
    tipoclienteid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoDieta(models.Model):
    tipoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_dieta'


class TipoEstudio(models.Model):
    tipoestudioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_estudio'


class TipoGlosa(models.Model):
    tipoglosaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_glosa'


class TipoIncidencia(models.Model):
    tipoincidenciaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_incidencia'


class TipoInformeConsulta(models.Model):
    tipoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_informe_consulta'


class TipoMantenimiento(models.Model):
    tipomantenimientoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_mantenimiento'


class TipoPaciente(models.Model):
    tipopacienteid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cuenta = models.CharField(max_length=15, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_paciente'


class TipoProducto(models.Model):
    tipoproductoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoProveedor(models.Model):
    tipoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_proveedor'


class TipoRetencion(models.Model):
    tiporetencionid = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_retencion'


class TmpAutorizacionPalic(models.Model):
    tmpid = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=50, blank=True, null=True)
    cups = models.CharField(max_length=10, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    mensaje = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_autorizacion_palic'


class TmpAutorizacionUniversal(models.Model):
    tmpid = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=50, blank=True, null=True)
    ordennd = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)
    cups = models.CharField(max_length=8, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    mensaje = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_autorizacion_universal'


class TmpExistencia(models.Model):
    productoid = models.IntegerField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_existencia'


class TmpRolAccion(models.Model):
    rolid = models.IntegerField()
    opcion_caption = models.CharField(max_length=100)
    opcion_name = models.CharField(max_length=100)
    inserta = models.IntegerField()
    modifica = models.IntegerField()
    elimina = models.IntegerField()
    seleccion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmp_rol_accion'


class Tomografia(models.Model):
    tomografiaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    estudioid = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    pacienteid = models.IntegerField(blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    patronid = models.IntegerField(blank=True, null=True)
    validado = models.IntegerField(blank=True, null=True)
    ordenmedicaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    detalleid = models.IntegerField(blank=True, null=True)
    usuarioid_tecnico = models.IntegerField(blank=True, null=True)
    fecha_estudio = models.DateTimeField(blank=True, null=True)
    medicoid_referidor = models.IntegerField(blank=True, null=True)
    validado_fecha = models.DateTimeField(blank=True, null=True)
    validado_hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tomografia'


class Transferencia(models.Model):
    transferenciaid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    almacenid_desde = models.IntegerField(blank=True, null=True)
    almacenid_hasta = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    requisicionid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    usuarioid_autoriza = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transferencia'


class TransferenciaDetalle(models.Model):
    transferenciaid = models.IntegerField(primary_key=True)
    detalleid = models.IntegerField()
    productoid = models.IntegerField(blank=True, null=True)
    servicioid = models.IntegerField(blank=True, null=True)
    medidaid = models.IntegerField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_vence = models.DateTimeField(blank=True, null=True)
    cantidad_requisicion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_ponderado = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'transferencia_detalle'
        unique_together = (('transferenciaid', 'detalleid'),)


class Triaje(models.Model):
    triajeid = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triaje'


class Turno(models.Model):
    turnoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    hora_inicio = models.DateTimeField(blank=True, null=True)
    hora_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno'


class Usuario(models.Model):
    usuarioid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    login_name = models.CharField(max_length=40, blank=True, null=True)
    clave = models.CharField(max_length=100, blank=True, null=True)
    rolid = models.IntegerField(blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)
    autoriza_credito_paciente = models.IntegerField(blank=True, null=True)
    autoriza_credito_empleado = models.IntegerField(blank=True, null=True)
    cobra_ambulatorio = models.IntegerField(blank=True, null=True)
    cobra_emergencia = models.IntegerField(blank=True, null=True)
    autoriza_credito_cliente = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    puerto_pos = models.CharField(max_length=50, blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    descuento_mayor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    empleadoid = models.IntegerField(blank=True, null=True)
    clave_resetear = models.IntegerField(blank=True, null=True)
    modifica_precio = models.IntegerField(blank=True, null=True)
    internacional_pago = models.IntegerField(blank=True, null=True)
    internacional_refacturacion = models.IntegerField(blank=True, null=True)
    internacional_cerrarcaso = models.IntegerField(blank=True, null=True)
    internacional_abrircaso = models.IntegerField(blank=True, null=True)
    pin = models.CharField(max_length=4, blank=True, null=True)
    auditor_externo = models.IntegerField()
    privado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioAlmacen(models.Model):
    usuarioid = models.IntegerField(primary_key=True)
    almacenid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_almacen'
        unique_together = (('usuarioid', 'almacenid'),)


class UsuarioDepartamento(models.Model):
    usuarioid = models.IntegerField(primary_key=True)
    departamentoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_departamento'
        unique_together = (('usuarioid', 'departamentoid'),)


class UsuarioGrid(models.Model):
    usuariogridid = models.AutoField(primary_key=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    form = models.CharField(max_length=100, blank=True, null=True)
    gridid = models.CharField(max_length=100, blank=True, null=True)
    detalle = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_grid'


class UsuarioSeguro(models.Model):
    usuarioseguroid = models.AutoField(primary_key=True)
    usuarioid = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='usuarioid')
    seguroid = models.ForeignKey(Seguro, models.DO_NOTHING, db_column='seguroid')

    class Meta:
        managed = False
        db_table = 'usuario_seguro'


class UsuarioServicio(models.Model):
    
    usuarioid = models.IntegerField(primary_key=True)
    servicioid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_servicio'
        unique_together = (('usuarioid', 'servicioid'),)


class VersionEjecutable(models.Model):
    versionid = models.AutoField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    dia = models.IntegerField(blank=True, null=True)
    hora = models.IntegerField(blank=True, null=True)
    mins = models.IntegerField(blank=True, null=True)
    segs = models.IntegerField(blank=True, null=True)
    actualiza = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_ejecutable'


class ViaAdministracion(models.Model):
    viaid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'via_administracion'
