# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class BillUsuario(models.Model):
    bill_id = models.PositiveIntegerField()
    usuario_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bill_usuario'


class Bills(models.Model):
    company_id = models.PositiveIntegerField()
    type_id = models.PositiveIntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    xml = models.TextField()
    metadata = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bills'


class CCodigopostal(models.Model):
    idc_codigopostal = models.AutoField(primary_key=True)
    cp = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(db_column='Ciudad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=70, blank=True, null=True)  # Field name made lowercase.
    zonahoraria = models.CharField(db_column='ZonaHoraria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horarioverano = models.DateField(db_column='HorarioVerano', blank=True, null=True)  # Field name made lowercase.
    diferenciaverano = models.CharField(db_column='DiferenciaVerano', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horarioinvierno = models.DateField(db_column='HorarioInvierno', blank=True, null=True)  # Field name made lowercase.
    inicioinvierno = models.CharField(db_column='InicioInvierno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diferenciainvierno = models.CharField(db_column='DiferenciaInvierno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    inicioverano = models.CharField(db_column='InicioVerano', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_codigopostal'


class Clients(models.Model):
    company_id = models.PositiveIntegerField()
    country_id = models.PositiveIntegerField()
    razon_social = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    numero_interior = models.CharField(max_length=255)
    numero_exterior = models.CharField(max_length=255)
    cp = models.CharField(max_length=5)
    colonia = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255)
    contacto_nombre = models.CharField(max_length=255, blank=True, null=True)
    contacto_apellido = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    email2 = models.CharField(max_length=255, blank=True, null=True)
    email3 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Companies(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255)
    key = models.TextField(blank=True, null=True)
    cert = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    dev = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Facturasdp(models.Model):
    idfacturadp = models.AutoField(db_column='IdFacturaDp', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=50)  # Field name made lowercase.
    rfcreceptor = models.CharField(db_column='RFCReceptor', max_length=15)  # Field name made lowercase.
    nombrereceptor = models.CharField(db_column='NombreReceptor', max_length=250)  # Field name made lowercase.
    rfcemisor = models.CharField(db_column='RFCEmisor', max_length=15)  # Field name made lowercase.
    nombreemisor = models.CharField(db_column='NombreEmisor', max_length=250)  # Field name made lowercase.
    rfcprovcertif = models.CharField(db_column='RFCProvCertif', max_length=15)  # Field name made lowercase.
    fechaticket = models.CharField(db_column='FechaTicket', max_length=15)  # Field name made lowercase.
    fechatimbrado = models.CharField(db_column='FechaTimbrado', max_length=15)  # Field name made lowercase.
    folio = models.CharField(db_column='Folio', max_length=20)  # Field name made lowercase.
    formapago = models.IntegerField(db_column='FormaPago')  # Field name made lowercase.
    metodopago = models.CharField(db_column='MetodoPago', max_length=3)  # Field name made lowercase.
    descuento = models.CharField(db_column='Descuento', max_length=1)  # Field name made lowercase.
    subtotal = models.FloatField(db_column='SubTotal')  # Field name made lowercase.
    total = models.FloatField(db_column='Total')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=1)  # Field name made lowercase.
    usocfdi = models.CharField(db_column='UsoCFDI', max_length=3)  # Field name made lowercase.
    nocertificadosat = models.CharField(db_column='NoCertificadoSAT', max_length=50)  # Field name made lowercase.
    path = models.CharField(db_column='Path', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facturasDP'


class Logs(models.Model):
    env = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    level = models.CharField(max_length=9)
    context = models.TextField()
    extra = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField()
    client_id = models.PositiveIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PermissionRole(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permission_role'
        unique_together = (('permission', 'role'),)


class Permissions(models.Model):
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class ReportesBills(models.Model):
    company_id = models.IntegerField()
    type_id = models.IntegerField()
    uuid = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    xml = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportes_bills'


class RoleUser(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_user'
        unique_together = (('user', 'role'),)


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SatMetodoPagos(models.Model):
    codigo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_metodo_pagos'


class Tokens(models.Model):
    bill_id = models.PositiveIntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'


class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Usuarios(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    rfc = models.CharField(max_length=13)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
