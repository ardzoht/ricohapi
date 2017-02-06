from django.db import models
from datetime import datetime

#  Create your models here.

#  Logs for each printer: These are all Integers, since they are numbers or codes
#  Coordinates X & Y are floats, for the nature of the number
class PrinterLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default = datetime.now)
    global_counter = models.IntegerField(default = 0)
    counter_print_bw = models.IntegerField(default = 0)
    counter_print_color = models.IntegerField(default = 0)
    counter_copy_bw = models.IntegerField(default = 0)
    counter_copy_color = models.IntegerField(default = 0)
    counter_bw_total = models.IntegerField(default = 0)
    counter_color_total = models.IntegerField(default = 0)
    fk_printer = models.CharField(max_length=15, default='W0123456789')
    counter_fax_bw = models.IntegerField(default = 0)
    counter_fax_color = models.IntegerField(default = 0)
    counter_toner_black = models.IntegerField(default = 0)
    counter_toner_cyan = models.IntegerField(default = 0)
    counter_toner_magenta = models.IntegerField(default = 0)
    counter_toner_yellow = models.IntegerField(default = 0)
    counter_duplex = models.IntegerField(default = 0)
    counter_DLT_bw = models.IntegerField(default = 0)
    counter_DLT_color = models.IntegerField(default = 0)
    counter_scan_jobs = models.IntegerField(default = 0)
    coordinate_X = models.FloatField(default = 28.698494)
    coordinate_Y = models.FloatField(default = -106.130584)

    def __unicode__(self):
        return str(self.fk_printer)

class Heartbeats(models.Model):
    imei = models.CharField(max_length=20)
    rssi = models.CharField(max_length=2)
    error = models.CharField(max_length=4)
    version = models.CharField(max_length=12)
    serial = models.CharField(primary_key=True, max_length=15)

    def __unicode__(self):
           return str(self.serial)
