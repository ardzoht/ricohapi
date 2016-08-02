import json
import requests
import datetime

class Log:

	def __init__(self, gc, cpbw, cpc, ccbw, ccc,cpt, cct, p_id, cfbw, cfc, tonblack, toncyan, tonmag, tonyell, cduplex):
		#define message slicing by protocol structure

		# Using dummy data for now
		self.global_counter = gc
		self.counter_print_bw = cpbw
		self.counter_print_color = cpc
		self.counter_copy_bw  = ccbw
		self.counter_copy_color = ccc
		self.counter_bw_total = cct
		self.counter_color_total = cpt
		self.fk_printer = p_id
		self.counter_fax_bw = cfbw
		self.counter_fax_color = cfc
		self.counter_toner_black = tonblack
		self.counter_toner_cyan = toncyan
		self.counter_toner_magenta = tonmag
		self.counter_toner_yellow = tonyell
		self.counter_duplex = cduplex

	def to_json(self):
		return json.dumps(self, default= lambda o: o.__dict__, sort_keys=True, indent=4)

	def upload(self):
		headers = {'Content-Type': "application/json"}
		r = requests.post("http://192.168.1.2:8081/api/logs/", data=self.to_json(),
        				  headers=headers)
		print self.to_json(), r.status_code


class MessageProcessor:

	def process_message(self, message):
		global_counter = 0
		counter_print_bw = 0
		counter_print_color = 0
		counter_copy_bw  = 0
		counter_copy_color = 0
		counter_fax_bw = 0
		counter_fax_color = 0
		counter_toner_black = 0
		counter_toner_cyan = 0
		counter_toner_magenta = 0
		counter_toner_yellow = 0
		counter_duplex = 0

		message_list = message.split('%')
		printer_id = message_list[1]
		print "P ID -> " + printer_id

		events = []
        
		try:
			info = []
			info = message_list
			date = info[2][:-6] + '2016' + info[2][6:]
			date = datetime.datetime.strptime(date, "%d%m%Y%H%M")
			info[0] = date
			global_counter = info[3]
			counter_print_color = info[4]
			counter_print_bw = info[5]
			counter_copy_color = info[6]
			counter_copy_bw = info[7]
			counter_fax_bw = info[8]
			counter_fax_color = info[9]
			counter_toner_black = info[10]
			counter_toner_cyan = info[11]
			counter_toner_magenta = info[12]
			counter_toner_yellow = info[13]
			counter_duplex = info[14]
			try:
				counter_color_total = int(counter_print_color) + int(counter_copy_color) + int(counter_fax_bw)
				counter_bw_total = int(counter_print_bw) + int(counter_copy_bw) + int(counter_fax_color)
			except Exception:
				counter_color_total = 0
				counter_bw_total = 0
				counter_color_total = 0
				counter_bw_total = 0
			events.append(info)

			print "Events -> ", events
			log = Log(global_counter, counter_print_bw, counter_print_color, counter_copy_bw, counter_copy_color, counter_color_total, counter_bw_total, printer_id, counter_fax_bw, counter_fax_color, counter_toner_black, counter_toner_cyan, counter_toner_magenta, counter_toner_yellow, counter_duplex)
			log.upload()
			return True

		except Exception:
			print "\nError with the current message: ", info
			print "Will continue with the procedure.\n"
			return False
