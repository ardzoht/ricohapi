from api.models import Printer, PrinterLog
from django.core.mail import send_mail

class SendEmailReport
	allObjects = PrinterLog.objects.all()
	
	for printerLog in allObjects:
		printerId = str(printerLog.fk_printer)
        copy_color_counter = str(printerLog.counter_copy_color)
        copy_black_white_counter = str(printerLog.counter_copy_bw) 
        print_color_counter = str(printerLog.counter_print_color)
        total_black_white = str(printerLog.counter_bw_total)
        total_color = str(printerLog.counter_color_total)
        print_black_white_counter = str(printerLog.counter_print_bw)
        fax_black_white_counter = str(printerLog.counter_fax_bw)
        fax_color_counter = str(printerLog.counter_fax_color)
        toner_black_counter = str(printerLog.counter_toner_black)
        toner_cyan_counter = str(counter_toner_cyan)
        toner_magenta_counter = str(printerLog.counter_toner_magenta)
        toner_yellow_counter = str(printerLog.counter_toner_yellow)	

        b = Printer.objects.get(printer_id=(print_id))
        email = b.emailReport
        emailsToSend = email.split(';')

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
        send_mail(subject, message, fromMail, emailsToSend, fail_silently=False)
