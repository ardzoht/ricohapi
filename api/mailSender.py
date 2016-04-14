from api.models import Printer, PrinterLog
from django.core.mail import send_mail

class SendEmailReport
	allObjects = PrinterLog.objects.all()
	
	for printerLog in allObjects:
		printerId = printerLog.fk_printer
                copy_color_counter = printerLog.counter_copy_color
           	copy_black_white_counter = printerLog.counter_copy_bw 
            	print_color_counter = printerLog.counter_print_color
            	total_black_white = printerLog.counter_bw_total
            	total_color = printerLog.counter_color_total
            	print_black_white_counter = printerLog.counter_print_bw
            	fax_black_white_counter = printerLog.counter_fax_bw
            	fax_color_counter = printerLog.counter_fax_color
            	toner_black_counter = printerLog.counter_toner_black
            	toner_cyan_counter = counter_toner_cyan
           	toner_magenta_counter = printerLog.counter_toner_magenta
            	toner_yellow_counter = printerLog.counter_toner_yellow	
