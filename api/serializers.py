from rest_framework.serializers import ModelSerializer, IntegerField, ReadOnlyField, CharField
from api.models import Printer, PrinterLog
from django.core.mail import send_mail
# Create your views here.

class PrinterSerializer(ModelSerializer):
	class Meta:
		model = Printer
		fields = ('printer_id', 'description', 'emailReport', 'cutDate', 'client')

class PrinterLogSerializer(ModelSerializer):
	log_id = ReadOnlyField()
	
        class Meta:
		model = PrinterLog
		fields = ('log_id', 'timestamp', 'global_counter', 'counter_print_bw', 'counter_print_color','counter_copy_bw', 'counter_copy_color','counter_bw_total', 'counter_color_total', 'fk_printer', 'counter_fax_bw', 'counter_fax_color', 'counter_toner_black', 'counter_toner_cyan', 'counter_toner_magenta', 'counter_toner_yellow')

        def save(self):
		fromMail = 'nfc.dev.cita@gmail.com' 
		globalCounter = str(self.validated_data['global_counter'])
		copy_color_counter = str(self.validated_data['counter_copy_color'])
		copy_black_white_counter = str(self.validated_data['counter_copy_bw'])
		print_color_counter = str(self.validated_data['counter_print_color'])
		total_black_white = str(self.validated_data['counter_bw_total'])
		total_color = str(self.validated_data['counter_color_total'])
		print_black_white_counter = str(self.validated_data['counter_print_bw'])
		print_id = str(self.validated_data['fk_printer'])
		fax_black_white_counter = str(self.validated_data['counter_fax_bw'])
		fax_color_counter = str(self.validated_data['counter_fax_color'])
		toner_black_counter = str(self.validated_data['counter_toner_black'])
		toner_cyan_counter = str(self.validated_data['counter_toner_cyan'])
		toner_magenta_counter = str(self.validated_data['counter_toner_magenta'])
		toner_yellow_counter = str(self.validated_data['counter_toner_yellow'])
		b = Printer.objects.get(printer_id=(print_id))
		email = b.emailReport
		emailsToSend = email.split(';')

            	obj = PrinterLog(global_counter=self.validated_data['global_counter'], counter_copy_color=self.validated_data['counter_copy_color'], counter_copy_bw=self.validated_data['counter_copy_bw'], counter_print_color=self.validated_data['counter_print_color'], counter_bw_total=self.validated_data['counter_bw_total'], counter_color_total=self.validated_data['counter_color_total'], counter_print_bw=self.validated_data['counter_print_bw'], fk_printer=self.validated_data['fk_printer'], counter_fax_bw=self.validated_data['counter_fax_bw'], counter_fax_color=self.validated_data['counter_fax_color'], counter_toner_black=self.validated_data['counter_toner_black'], counter_toner_cyan=self.validated_data['counter_toner_cyan'], counter_toner_magenta=self.validated_data['counter_toner_magenta'], counter_toner_yellow=self.validated_data['counter_toner_yellow'])
            	obj.save()
            
            	if toner_black_counter == "-3":
                	toner_black_counter = "Level OK: over 10%% to 100%%"
            	elif toner_black_counter == "-100":
                	toner_black_counter = "Low Level: under 10%% of toner"
            
            	if toner_cyan_counter == "-3": 
                	toner_cyan_counter = "Level OK: over 10%% to 100%%"
            	elif toner_cyan_counter == "-100":
                	toner_cyan_counter = "Low Level: under 10%% of toner"
            
            	if toner_magenta_counter == "-3":
                	toner_magenta_counter = "Level OK: over 10%% to 100%%"
            	elif toner_magenta_counter == "-100":
               		toner_magenta_counter = "Low Level: under 10%% of toner"
            
            	if toner_yellow_counter == "-3":
                	toner_yellow_counter = "Level OK: over 10%% to 100%%"
            	elif toner_yellow_counter == "-100":
                	toner_yellow_counter = "Low Level: under 10%% of toner"

            	if toner_black_counter == "200":
                	toner_black_counter = "Couldn't retrieve this data"
            	if toner_cyan_counter == "200":
                	toner_cyan_counter = "Couldn't retrieve this data"
            	if toner_magenta_counter == "200":
                	toner_magenta_counter = "Couldn't retrieve this data"
            	if toner_yellow_counter == "200":
                	toner_yellow_counter = "Couldn't retrieve this data"
            
            	if total_color == "200":
                	total_color = "0"
            	if fax_black_white_counter == "200":
                	fax_black_white_counter = "0"
            	if fax_color_counter == "200":
                	fax_color_counter = "0"
             
            	message = "The current counters of the MFP (" + print_id + ") are the following: " + "\n\nTotal B&W: " + total_black_white + "\nTotal Color: " + total_color + "\nPrinter B&W Counter: " + print_black_white_counter + "\nPrinter Color Counter: " + print_color_counter + "\nCopier B&W Counter: " + copy_black_white_counter + "\nCopier Color Counter: " + copy_color_counter + "\nFax B&W Counter: " + fax_black_white_counter + "\nFax Color Counter: " + fax_color_counter + "\nBlack Toner Counter: " + toner_black_counter + "\nCyan Toner Counter: " + toner_cyan_counter + "\nMagenta Toner Counter: " + toner_magenta_counter + "\nYellow Toner Counter: " + toner_yellow_counter 
            	subject = "MPF Counters Update: " + print_id + ""
            	#send_mail(subject, message, fromMail, ['raime.bustos@gmail.com','antonio-hdez@live.com','carlos.me@outlook.com','dave.saenz.1892@gmail.com'], fail_silently=False) 
            	send_mail(subject, message, fromMail, emailsToSend, fail_silently=False)
