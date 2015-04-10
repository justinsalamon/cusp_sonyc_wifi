from django.db import models

class Scan(models.Model):
  idx = models.AutoField(primary_key=True)
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

  def __unicode__(self):
    return self.ssid
