from django.db import models

# Create your models here.

#For each printer
class Printer(models.Model):
    printer_id = models.IntegerField(primary_key=True)
    global_counter = models.IntegerField()
    counter_print_bw = models.IntegerField()
    counter_print_color = models.IntegerField()
    counter_copy_bw = models.IntegerField()
    counter_copy_color = models.IntegerField()

    def __unicode__(self):
	return str(printer_id)	    
    
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=40)
    user_total_counter = models.IntegerField()
    user_counter_print_bw = models.IntegerField()
    user_counter_print_color = models.IntegerField()
    user_counter_copy_bw = models.IntegerField()
    user_counter_copy_color = models.IntegerField()
    printers = models.ManyToManyField(Printer)

    def __unicode__(self):
    	return str(user_name)
