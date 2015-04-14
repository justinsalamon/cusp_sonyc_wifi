# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Boats(models.Model):
    bid = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Boats'


class Reserves(models.Model):
    sid = models.IntegerField()
    bid = models.IntegerField()
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'Reserves'
        unique_together = (('sid', 'bid', 'day'),)


class Sailors(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=30, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sailors'


class Alltrips(models.Model):
    medallion = models.CharField(max_length=50, blank=True, null=True)
    hack_license = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.CharField(max_length=3, blank=True, null=True)
    pickup_datetime = models.DateTimeField()
    rate_code = models.SmallIntegerField(blank=True, null=True)
    store_and_fwd_flag = models.CharField(max_length=3, blank=True, null=True)
    dropoff_datetime = models.DateTimeField()
    passenger_count = models.SmallIntegerField(blank=True, null=True)
    trip_time_in_secs = models.IntegerField(blank=True, null=True)
    trip_distance = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    pickup_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    pickup_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    payment_type = models.CharField(max_length=3, blank=True, null=True)
    fare_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    surcharge = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    mta_tax = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tip_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tolls_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alltrips'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class BooksBooks(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    read = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'books_books'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class Fares(models.Model):
    medallion = models.CharField(max_length=50, blank=True, null=True)
    hack_license = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.CharField(max_length=3, blank=True, null=True)
    pickup_datetime = models.DateTimeField()
    payment_type = models.CharField(max_length=3, blank=True, null=True)
    fare_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    surcharge = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    mta_tax = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tip_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tolls_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fares'


class Medallions(models.Model):
    medallion = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    current_status = models.CharField(max_length=10, blank=True, null=True)
    dmv_license_plate = models.CharField(db_column='DMV_license_plate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vehicle_vin_number = models.CharField(db_column='vehicle_VIN_number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vehicle_type = models.CharField(max_length=10, blank=True, null=True)
    model_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    medallion_type = models.CharField(max_length=30, blank=True, null=True)
    agent_number = models.IntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=30, blank=True, null=True)
    agent_telephone_number = models.CharField(max_length=15, blank=True, null=True)
    agent_website = models.CharField(max_length=50, blank=True, null=True)
    agent_address = models.CharField(max_length=50, blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    last_updated_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medallions'


class Trips(models.Model):
    medallion = models.CharField(max_length=50, blank=True, null=True)
    hack_license = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.CharField(max_length=3, blank=True, null=True)
    rate_code = models.SmallIntegerField(blank=True, null=True)
    store_and_fwd_flag = models.CharField(max_length=3, blank=True, null=True)
    pickup_datetime = models.DateTimeField()
    dropoff_datetime = models.DateTimeField()
    passenger_count = models.SmallIntegerField(blank=True, null=True)
    trip_time_in_secs = models.IntegerField(blank=True, null=True)
    trip_distance = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    pickup_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    pickup_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'


class Tripwithlicense(models.Model):
    medallion = models.CharField(max_length=50, blank=True, null=True)
    hack_license = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.CharField(max_length=3, blank=True, null=True)
    pickup_datetime = models.DateTimeField()
    rate_code = models.SmallIntegerField(blank=True, null=True)
    store_and_fwd_flag = models.CharField(max_length=3, blank=True, null=True)
    dropoff_datetime = models.DateTimeField()
    passenger_count = models.SmallIntegerField(blank=True, null=True)
    trip_time_in_secs = models.IntegerField(blank=True, null=True)
    trip_distance = models.DecimalField(max_digits=12, decimal_places=5, blank=True, null=True)
    pickup_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    pickup_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    dropoff_latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    payment_type = models.CharField(max_length=3, blank=True, null=True)
    fare_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    surcharge = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    mta_tax = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tip_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    tolls_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    current_status = models.CharField(max_length=10, blank=True, null=True)
    dmv_license_plate = models.CharField(db_column='DMV_license_plate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vehicle_vin_number = models.CharField(db_column='vehicle_VIN_number', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vehicle_type = models.CharField(max_length=10, blank=True, null=True)
    model_year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    medallion_type = models.CharField(max_length=30, blank=True, null=True)
    agent_number = models.IntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=30, blank=True, null=True)
    agent_telephone_number = models.CharField(max_length=15, blank=True, null=True)
    agent_website = models.CharField(max_length=50, blank=True, null=True)
    agent_address = models.CharField(max_length=50, blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    last_updated_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tripwithlicense'


class WifiScan(models.Model):
    idx = models.BigIntegerField(primary_key=True)
    lat = models.FloatField()
    lng = models.FloatField()
    acc = models.FloatField()
    altitude = models.FloatField()
    time = models.DecimalField(max_digits=15, decimal_places=0)
    device_mac = models.CharField(max_length=20)
    app_version = models.CharField(max_length=10)
    droid_version = models.CharField(max_length=10)
    device_model = models.CharField(max_length=50)
    ssid = models.CharField(max_length=100)
    bssid = models.CharField(max_length=20)
    caps = models.CharField(max_length=100)
    level = models.FloatField()
    freq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wifi_scan'
