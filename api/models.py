['*']
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barang(models.Model):
    idbarang = models.CharField(primary_key=True, max_length=10)
    idbarangmanual = models.CharField(max_length=15, blank=True, null=True)
    idgolongan = models.IntegerField(blank=True, null=True)
    barang = models.CharField(max_length=40, blank=True, null=True)
    stok = models.IntegerField(blank=True, null=True)
    keterangan = models.CharField(max_length=30, blank=True, null=True)
    idsatuan = models.IntegerField(blank=True, null=True)
    idterkecil = models.IntegerField(blank=True, null=True)
    nilai_kon = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    valuenya = models.FloatField(blank=True, null=True)
    hpp = models.FloatField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)
    qtyambil = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_barang'


class Catatan(models.Model):
    id = models.AutoField(primary_key=True)
    keterangan = models.CharField(max_length=30, blank=True, null=True)
    charge = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_catatan'


class Detailcontrol(models.Model):
    room = models.CharField(max_length=6, blank=True, null=True)
    jamtgl = models.DateTimeField(blank=True, null=True)
    iduser = models.CharField(max_length=5, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_detailcontrol'


class Golongan(models.Model):
    idgol = models.IntegerField(blank=True, null=True)
    golongan = models.CharField(max_length=30, blank=True, null=True)
    kode = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_golongan'


class Hitory(models.Model):
    idbarang = models.CharField(max_length=10)
    idmenu = models.CharField(max_length=10)
    idorder = models.CharField(max_length=10)
    idorderpo = models.CharField(max_length=11)
    inya = models.PositiveSmallIntegerField()
    outnya = models.PositiveSmallIntegerField()
    tgl = models.DateTimeField()
    palue = models.FloatField()

    class Meta:
        managed = False
        db_table = '_hitory'


class Komposisi(models.Model):
    idmenu = models.CharField(max_length=10, blank=True, null=True)
    idbarang = models.CharField(max_length=10, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    satuan = models.IntegerField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_komposisi'


class Logstok(models.Model):
    idlog = models.CharField(primary_key=True, max_length=11)
    idbarang = models.CharField(max_length=10)
    tanggal = models.DateTimeField()
    stok = models.PositiveIntegerField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    ket = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_logstok'


class Ordersup(models.Model):
    idorder = models.CharField(max_length=12, blank=True, null=True)
    supplier = models.CharField(max_length=30, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_ordersup'


class Paket(models.Model):
    idpaket = models.CharField(max_length=7, blank=True, null=True)
    idmenu = models.CharField(max_length=7, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_paket'


class Pooutlet(models.Model):
    idpo = models.CharField(max_length=12, blank=True, null=True)
    idbarang = models.CharField(max_length=15, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    qtyorder = models.IntegerField(blank=True, null=True)
    qtyterima = models.IntegerField(blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tgl_order = models.DateTimeField(blank=True, null=True)
    idsatuan = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_pooutlet'


class Satuan(models.Model):
    idsatuan = models.IntegerField()
    satuan = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_satuan'


class Torder(models.Model):
    idorder = models.CharField(max_length=12, blank=True, null=True)
    suratjalan = models.CharField(max_length=12, blank=True, null=True)
    invoice = models.CharField(max_length=12, blank=True, null=True)
    idbarang = models.CharField(max_length=15, blank=True, null=True)
    qty_order = models.IntegerField(blank=True, null=True)
    qty_terima = models.IntegerField(blank=True, null=True)
    harga_order = models.FloatField()
    harga_invoice = models.FloatField(blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tgl_invoice = models.DateTimeField(blank=True, null=True)
    idpo = models.CharField(max_length=12, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_torder'


class Value(models.Model):
    idlog = models.CharField(max_length=10, blank=True, null=True)
    idbarang = models.CharField(max_length=10, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    hsatuan = models.FloatField(blank=True, null=True)
    valuenya = models.FloatField(blank=True, null=True)
    tglnya = models.DateTimeField(blank=True, null=True)
    ket = models.IntegerField(blank=True, null=True)
    refrensi = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_value'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Booking(models.Model):
    idbook = models.IntegerField()
    nama = models.CharField(max_length=30, blank=True, null=True)
    notelp1 = models.CharField(db_column='Notelp1', max_length=14, blank=True, null=True)  # Field name made lowercase.
    notelp2 = models.CharField(db_column='Notelp2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    idkategoriroom = models.IntegerField(blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    jmlorang = models.IntegerField(blank=True, null=True)
    durasi = models.IntegerField(blank=True, null=True)
    keterangan = models.CharField(db_column='Keterangan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglsortir = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dp = models.FloatField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    idorder = models.CharField(max_length=10, blank=True, null=True)
    idkasir = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


class Cardtype(models.Model):
    idcard = models.SmallIntegerField(blank=True, null=True)
    namacard = models.CharField(max_length=30, blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cardtype'


class Comm(models.Model):
    idcom = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    comm = models.CharField(max_length=150)
    room = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'comm'


class CustomPlaylist(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nama = models.CharField(max_length=255, blank=True, null=True)
    deskripsi = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_playlist'


class CustomPlaylistDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idlagu = models.IntegerField(blank=True, null=True)
    idplaylist = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_playlist_detail'


class Datapropertis(models.Model):
    maksid = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'datapropertis'


class Detailrequest(models.Model):
    artis = models.CharField(max_length=255, blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    tujuan = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    idreq = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailrequest'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Edp(models.Model):
    idedp = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    aktif = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edp'


class Exv(models.Model):
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    artist = models.CharField(db_column='Artist', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'exv'

class Hitlagu(models.Model):
    idhit = models.AutoField(primary_key=True)
    idlagu = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    date_play = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hitlagu'


class Idrequest(models.Model):
    idrequest = models.CharField(max_length=10, db_collation='utf8_bin', blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    artist = models.CharField(db_column='Artist', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(blank=True, null=True)
    tujuan = models.CharField(max_length=15, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=15, blank=True, null=True)
    tglubah = models.DateField(db_column='TglUbah', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'idrequest'


class Instrument(models.Model):
    idins = models.IntegerField(primary_key=True)
    namains = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrument'


class Jenis(models.Model):
    idjenis = models.AutoField(primary_key=True)
    jenis = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jenis'


class JualMenu(models.Model):
    noorder = models.CharField(max_length=10, db_collation='latin1_swedish_ci', blank=True, null=True)
    idmenu = models.CharField(max_length=10, db_collation='latin1_swedish_ci', blank=True, null=True)
    harga_asli = models.FloatField(blank=True, null=True)
    harga_jual = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    timeorder = models.DateTimeField(blank=True, null=True)
    waiters = models.CharField(max_length=5, db_collation='latin1_swedish_ci', blank=True, null=True)
    catatan = models.CharField(max_length=30, db_collation='latin1_swedish_ci', blank=True, null=True)
    co = models.CharField(max_length=12, db_collation='latin1_swedish_ci', blank=True, null=True)
    cancel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jual_menu'


class JualOther(models.Model):
    idorder = models.CharField(max_length=10, blank=True, null=True)
    namaother = models.CharField(max_length=15, blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    dateorder = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jual_other'


class JualRoom(models.Model):
    idorder = models.CharField(max_length=10, blank=True, null=True)
    idroom = models.IntegerField(blank=True, null=True)
    durasi = models.IntegerField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    tglawal = models.DateTimeField(blank=True, null=True)
    tglakhir = models.DateTimeField(blank=True, null=True)
    idjam = models.IntegerField(blank=True, null=True)
    keterangan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jual_room'


class Kamar(models.Model):
    idkamar = models.IntegerField()
    namakamar = models.CharField(max_length=10, blank=True, null=True)
    kategorikamar = models.IntegerField(blank=True, null=True)
    orderid = models.CharField(max_length=10, blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    atasnama = models.CharField(max_length=20, blank=True, null=True)
    idmember = models.CharField(max_length=10, blank=True, null=True)
    orang = models.IntegerField(blank=True, null=True)
    durasi = models.IntegerField(blank=True, null=True)
    totalroom = models.FloatField(blank=True, null=True)
    totalmenu = models.FloatField(blank=True, null=True)
    totallain = models.FloatField(blank=True, null=True)
    catatan = models.CharField(max_length=20, blank=True, null=True)
    statuschekin = models.IntegerField(blank=True, null=True)
    jual = models.IntegerField(blank=True, null=True)
    checkroom = models.SmallIntegerField(blank=True, null=True)
    chekout = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kamar'


class Katkamar(models.Model):
    kategorikamar = models.IntegerField()
    kelas = models.CharField(max_length=10, blank=True, null=True)
    nh_day = models.FloatField(db_column='NH_day', blank=True, null=True)  # Field name made lowercase.
    hh_day = models.FloatField(db_column='HH_day', blank=True, null=True)  # Field name made lowercase.
    nh_end = models.FloatField(db_column='NH_end', blank=True, null=True)  # Field name made lowercase.
    hh_end = models.FloatField(db_column='HH_end', blank=True, null=True)  # Field name made lowercase.
    hd = models.FloatField(db_column='HD', blank=True, null=True)  # Field name made lowercase.
    lpromo = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=30, blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'katkamar'


class Lagu(models.Model):
    idlagu = models.PositiveIntegerField(primary_key=True)
    edp = models.IntegerField()
    dup = models.CharField(max_length=20)
    judul = models.CharField(max_length=255)
    artis = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    cont = models.CharField(max_length=4)
    dur = models.TimeField()
    size = models.CharField(max_length=11)
    voc = models.IntegerField()
    xvoc = models.IntegerField()
    gol = models.IntegerField()
    jenis = models.IntegerField()
    vol = models.IntegerField()
    vol2 = models.IntegerField()
    vol3 = models.IntegerField()
    rms = models.DecimalField(max_digits=5, decimal_places=2)
    rms2 = models.DecimalField(max_digits=5, decimal_places=2)
    rms3 = models.DecimalField(max_digits=5, decimal_places=2)
    hits = models.IntegerField()
    new = models.IntegerField()
    popular = models.IntegerField()
    idsource = models.IntegerField()
    datetime = models.DateTimeField(blank=True, null=True)
    hade = models.IntegerField()
    judul2 = models.CharField(max_length=255)
    judul3 = models.CharField(max_length=255)
    exjudul = models.CharField(max_length=255)
    artis2 = models.CharField(max_length=255)
    artis3 = models.CharField(max_length=255)
    exartis = models.CharField(max_length=255)
    rev = models.PositiveSmallIntegerField()
    keterangan = models.CharField(max_length=255)
    masalah = models.PositiveSmallIntegerField()
    drive = models.PositiveSmallIntegerField()
    status = models.IntegerField()
    posisi = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'lagu'


class LaguOutlet(models.Model):
    idlagu = models.PositiveIntegerField(primary_key=True)
    edp = models.IntegerField(blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    artis = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    voc = models.IntegerField(blank=True, null=True)
    xvoc = models.IntegerField(blank=True, null=True)
    gol = models.IntegerField(blank=True, null=True)
    jenis = models.IntegerField(blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    vol2 = models.IntegerField(blank=True, null=True)
    vol3 = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    new = models.IntegerField(blank=True, null=True)
    popular = models.IntegerField(blank=True, null=True)
    idsource = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    hade = models.IntegerField(blank=True, null=True)
    judul2 = models.CharField(max_length=255, blank=True, null=True)
    judul3 = models.CharField(max_length=255, blank=True, null=True)
    exjudul = models.CharField(max_length=255, blank=True, null=True)
    artis2 = models.CharField(max_length=255, blank=True, null=True)
    artis3 = models.CharField(max_length=255, blank=True, null=True)
    exartis = models.CharField(max_length=255, blank=True, null=True)
    posisi = models.PositiveSmallIntegerField()
    keterangan = models.CharField(max_length=255, blank=True, null=True)
    masalah = models.PositiveSmallIntegerField(blank=True, null=True)
    drive = models.PositiveSmallIntegerField(blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lagu_outlet'


class Logpulsa(models.Model):
    barcode = models.CharField(db_column='Barcode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    invoice = models.CharField(max_length=12, blank=True, null=True)
    awal = models.FloatField(blank=True, null=True)
    pakai = models.FloatField(blank=True, null=True)
    transaksi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logpulsa'


class Mapping(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    usermapp = models.CharField(db_column='userMapp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    passmapp = models.CharField(db_column='passMapp', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapping'


class MenuCancel(models.Model):
    noorder = models.CharField(max_length=10, blank=True, null=True)
    idmenu = models.CharField(max_length=10, blank=True, null=True)
    harga_asli = models.FloatField(blank=True, null=True)
    harga_jual = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    qty = models.IntegerField(blank=True, null=True)
    timeorder = models.DateTimeField(blank=True, null=True)
    waiters = models.CharField(max_length=5, blank=True, null=True)
    catatan = models.CharField(max_length=30, blank=True, null=True)
    co = models.CharField(max_length=12, blank=True, null=True)
    kasir = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_cancel'


class Outlet(models.Model):
    nama = models.CharField(max_length=45)
    ip = models.CharField(max_length=100)
    db = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outlet'


class Pilem(models.Model):
    idpilem = models.PositiveIntegerField(primary_key=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    stpilem = models.PositiveIntegerField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    vol = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pilem'


class Playlist(models.Model):
    idlagu = models.PositiveIntegerField()
    namaroom = models.CharField(max_length=10, blank=True, null=True)
    idplaylist = models.IntegerField()
    ukey = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlist'


class Promo(models.Model):
    idpromo = models.CharField(max_length=10)
    namapromo = models.CharField(max_length=30, blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    menu = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(blank=True, null=True)
    service = models.IntegerField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)
    hapus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promo'


class Promoslide(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promoslide'


class Rating(models.Model):
    idlagu = models.PositiveIntegerField(primary_key=True)
    rating = models.PositiveIntegerField()
    popolar = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class Req(models.Model):
    idreq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    artist = models.CharField(max_length=45)
    title = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'req'


class Requestlagu(models.Model):
    idreq = models.CharField(db_column='idReq', primary_key=True, max_length=10)  # Field name made lowercase.
    tglinput = models.DateTimeField(blank=True, null=True)
    edp = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requestlagu'


class Room(models.Model):
    idroom = models.SmallAutoField(primary_key=True)
    namaroom = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    players = models.PositiveIntegerField()
    volmaster = models.PositiveIntegerField(blank=True, null=True)
    jam = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    durasi = models.PositiveSmallIntegerField(blank=True, null=True)
    panggil = models.PositiveSmallIntegerField(blank=True, null=True)
    mac = models.CharField(max_length=30, blank=True, null=True)
    waktu = models.PositiveSmallIntegerField(blank=True, null=True)
    addtime = models.PositiveSmallIntegerField(blank=True, null=True)
    idandro = models.CharField(max_length=6, blank=True, null=True)
    lastid = models.CharField(max_length=5, blank=True, null=True)
    ip = models.CharField(max_length=30, blank=True, null=True)
    kondisi = models.IntegerField(blank=True, null=True)
    callopr = models.IntegerField(blank=True, null=True)
    calltime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Runtext(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    katakata = models.CharField(max_length=200, blank=True, null=True)
    tujuan = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtext'


class Setup(models.Model):
    taxroom = models.FloatField(blank=True, null=True)
    serviceroom = models.FloatField(blank=True, null=True)
    taxmenu = models.FloatField(blank=True, null=True)
    servicemenu = models.FloatField(blank=True, null=True)
    taxother = models.FloatField(blank=True, null=True)
    serviceother = models.FloatField(blank=True, null=True)
    idoutlet = models.CharField(db_column='idOutlet', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(max_length=20, blank=True, null=True)
    promo = models.IntegerField(blank=True, null=True)
    fmc = models.IntegerField(blank=True, null=True)
    weekend = models.IntegerField(blank=True, null=True)
    hpromo = models.SmallIntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    tipehitung = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setup'


class Setuppajak(models.Model):
    taxroom = models.FloatField(blank=True, null=True)
    serviceroom = models.FloatField(blank=True, null=True)
    taxmenu = models.FloatField(blank=True, null=True)
    servicemenu = models.FloatField(blank=True, null=True)
    taxother = models.FloatField(blank=True, null=True)
    serviceother = models.FloatField(blank=True, null=True)
    idoutlet = models.CharField(db_column='idOutlet', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nama = models.CharField(max_length=20, blank=True, null=True)
    promo = models.IntegerField(blank=True, null=True)
    fmc = models.IntegerField(blank=True, null=True)
    weekend = models.IntegerField(blank=True, null=True)
    hpromo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setuppajak'


class Setupurl(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    rootpath = models.CharField(max_length=255, blank=True, null=True)
    idbooth = models.CharField(max_length=5, blank=True, null=True)
    ket = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setupurl'


class Setupuser(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.TextField(blank=True, null=True)
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    status = models.IntegerField(blank=True, null=True)
    waktu = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setupuser'


class Source(models.Model):
    idsource = models.AutoField(primary_key=True)
    namasource = models.CharField(db_column='namaSource', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'source'


class Svrpublic(models.Model):
    idoutlet = models.AutoField(primary_key=True)
    outlet = models.CharField(max_length=45)
    ipnya = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'svrpublic'


class Tbank(models.Model):
    id = models.AutoField(primary_key=True)
    namabank = models.CharField(max_length=15, blank=True, null=True)
    keterangan = models.CharField(max_length=10, blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbank'


class Tbarang(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(db_column='Nama', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ket = models.CharField(max_length=50, blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True, null=True)
    tgl_beli = models.DateTimeField(blank=True, null=True)
    tgl_akhir = models.DateTimeField(blank=True, null=True)
    harga_aw = models.FloatField(blank=True, null=True)
    harga_ak = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbarang'


class Tbayar(models.Model):
    invoice = models.CharField(max_length=12, blank=True, null=True)
    sah = models.IntegerField(blank=True, null=True)
    btotal = models.FloatField(blank=True, null=True)
    bcash = models.FloatField(blank=True, null=True)
    bcard = models.FloatField(blank=True, null=True)
    bmember = models.FloatField(blank=True, null=True)
    jenis = models.IntegerField(blank=True, null=True)
    bank = models.IntegerField(blank=True, null=True)
    nocc = models.CharField(max_length=20, blank=True, null=True)
    namakartu = models.CharField(max_length=30, blank=True, null=True)
    barcode = models.CharField(max_length=15, blank=True, null=True)
    keterangan = models.CharField(max_length=30, blank=True, null=True)
    jamtgl = models.DateTimeField(blank=True, null=True)
    kasir = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbayar'


class TblForm(models.Model):
    kd_menu = models.CharField(max_length=3, blank=True, null=True)
    namamenu = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_form'


class TblPrivilage(models.Model):
    idhak = models.IntegerField(blank=True, null=True)
    kd_menu = models.CharField(db_column='Kd_menu', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_privilage'


class Tkaryawan(models.Model):
    idkaryawan = models.CharField(max_length=5, db_collation='latin1_swedish_ci')
    idkategorikaryawan = models.IntegerField(blank=True, null=True)
    nama = models.CharField(max_length=20, db_collation='latin1_swedish_ci', blank=True, null=True)
    alamat = models.CharField(max_length=50, db_collation='latin1_swedish_ci', blank=True, null=True)
    telp = models.CharField(max_length=13, db_collation='latin1_swedish_ci', blank=True, null=True)
    hp = models.CharField(max_length=13, db_collation='latin1_swedish_ci', blank=True, null=True)
    tempatlahir = models.CharField(max_length=15, db_collation='latin1_swedish_ci', blank=True, null=True)
    tgllahir = models.DateTimeField(blank=True, null=True)
    tglkerja = models.DateTimeField(blank=True, null=True)
    agama = models.IntegerField(blank=True, null=True)
    statuskawin = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=10, db_collation='latin1_swedish_ci', blank=True, null=True)
    loginid = models.CharField(max_length=10, db_collation='latin1_swedish_ci', blank=True, null=True)
    haklogin = models.IntegerField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    onn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tkaryawan'


class Tkategorikaryawan(models.Model):
    idkategorikaryawan = models.IntegerField()
    kategori = models.CharField(max_length=15, blank=True, null=True)
    ketarangan = models.CharField(max_length=20, blank=True, null=True)
    kode = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tkategorikaryawan'


class Tkategorimenu(models.Model):
    id = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=30, blank=True, null=True)
    kode = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tkategorimenu'


class Tlagu(models.Model):
    invoice = models.CharField(max_length=12, blank=True, null=True)
    idlagu = models.CharField(max_length=5, blank=True, null=True)
    judul = models.CharField(max_length=40, blank=True, null=True)
    artis = models.CharField(max_length=30, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tlagu'


class Tlevelmember(models.Model):
    idlevel = models.CharField(max_length=10)
    namalevel = models.CharField(max_length=25, blank=True, null=True)
    discroom = models.FloatField(blank=True, null=True)
    discmenu = models.FloatField(blank=True, null=True)
    discother = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tlevelmember'


class Tmember(models.Model):
    idmember = models.CharField(max_length=10, blank=True, null=True)
    idlevel = models.IntegerField(blank=True, null=True)
    nama = models.CharField(max_length=30, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    telp = models.CharField(max_length=13, blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    ultah = models.DateTimeField(blank=True, null=True)
    startmember = models.DateTimeField(blank=True, null=True)
    endmember = models.DateTimeField(blank=True, null=True)
    barcode = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmember'


class Tmenu(models.Model):
    idmenu = models.CharField(max_length=7, db_collation='utf8_general_ci', blank=True, null=True)
    idkategori = models.IntegerField(blank=True, null=True)
    idpost = models.IntegerField(blank=True, null=True)
    menu = models.CharField(max_length=60, blank=True, null=True)
    totalkomposisi = models.FloatField(blank=True, null=True)
    terbuang = models.FloatField(blank=True, null=True)
    biayalain = models.FloatField(blank=True, null=True)
    totalbiaya = models.FloatField(blank=True, null=True)
    fmarkup = models.FloatField(blank=True, null=True)
    hargajual = models.FloatField(blank=True, null=True)
    grossmargin = models.FloatField(blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)
    nilai_bonus = models.FloatField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    paket = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmenu'


class Token(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    token = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class Tpanggilan(models.Model):
    idroom = models.IntegerField(blank=True, null=True)
    idpanggil = models.IntegerField(blank=True, null=True)
    tangal = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpanggilan'


class Tpostorder(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.CharField(max_length=10, blank=True, null=True)
    ippost = models.CharField(max_length=15, blank=True, null=True)
    aktive = models.IntegerField(blank=True, null=True)
    keterangan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpostorder'


class Tpulsa(models.Model):
    barcode = models.CharField(max_length=15)
    pulsa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpulsa'


class Transaksi(models.Model):
    idorder = models.CharField(max_length=10)
    invoice = models.CharField(unique=True, max_length=12, blank=True, null=True)
    tglmulai = models.DateTimeField(blank=True, null=True)
    tglakhir = models.DateTimeField(blank=True, null=True)
    idroom = models.IntegerField(blank=True, null=True)
    nama = models.CharField(max_length=60, blank=True, null=True)
    orang = models.IntegerField(blank=True, null=True)
    durasi = models.IntegerField(blank=True, null=True)
    memberid = models.CharField(max_length=10, blank=True, null=True)
    payment = models.IntegerField(blank=True, null=True)
    totalmenu = models.FloatField(blank=True, null=True)
    totalroom = models.FloatField(blank=True, null=True)
    totaldll = models.FloatField(blank=True, null=True)
    dismenu = models.FloatField(blank=True, null=True)
    disroom = models.FloatField(blank=True, null=True)
    disdll = models.FloatField(blank=True, null=True)
    dimember = models.FloatField(blank=True, null=True)
    voucher = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    service = models.FloatField(blank=True, null=True)
    kasir = models.CharField(max_length=10, blank=True, null=True)
    alasan = models.CharField(max_length=40, blank=True, null=True)
    pj = models.IntegerField(blank=True, null=True)
    ubah = models.IntegerField(blank=True, null=True)
    idpromo = models.CharField(max_length=10, blank=True, null=True)
    dp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaksi'


class Trecord(models.Model):
    invoice = models.CharField(max_length=12, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    customer = models.CharField(max_length=25, blank=True, null=True)
    arranger = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trecord'


class Tujuanrequest(models.Model):
    idtujuan = models.PositiveSmallIntegerField(blank=True, null=True)
    tujuan = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tujuanrequest'


class Tv(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255, blank=True, null=True)
    canel = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tv'


class Tweekend(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweekend'


class Updatelagu(models.Model):
    idupdate = models.CharField(max_length=6)
    tgl = models.DateTimeField()
    idlogin = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'updatelagu'
