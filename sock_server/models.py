import json
import requests
import datetime

class Log:

	def __init__(self, gc, cpbw, cpc, ccbw, ccc, cpt, cct, p_id):
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

	def to_json(self):
		return json.dumps(self, default= lambda o: o.__dict__, sort_keys=True, indent=4)

	def upload(self):
		headers = {'Content-Type': "application/json"}
		r = requests.post("http://riego.chi.itesm.mx:8081/api/logs/", data=self.to_json(), 
        				  headers=headers)
		print self.to_json(), r.status_code

class User:

	def __init__(self, message=None):
		#efine message slicing by protocol structure

		#Using dummy data 
		self.total_counter = 0
		self.user_counter_print_bw = 0
		self.user_counter_print_color = 0
		self.user_counter_copy_bw = 0
		self.user_counter_copy_color = 0

	def to_json(self):
		return json.dumps(self, default = lambda o:o.__dict__, sort_keys=True, indent=4)

	def upload(self):
		headers = {'Content-Type': "application/json"}
		r = requests.post("http://riego.chi.itesm.mx:8081/api/users/", data=self.to_json(),
						  headers=headers)
		print self.to_json(), r.status_code

class MessageProcessor:

	def process_message(self, message):
		global_counter = 0
		counter_print_bw = 0
		counter_print_color = 0
		counter_copy_bw  = 0
		counter_copy_color = 0

		message_list = message.split('\n')
		header = message_list[0]
		printer_id = header.split('%')[1]
		print "P ID -> " + printer_id
		
		events = []
		for line in message_list[1:-1]:
			info = line.split('%')
			date = info[0][:-6] + '2015' + info[0][6:]
			date = datetime.datetime.strptime(date, "%d%m%Y%H%M")
			info[0] = date
			user = info[1]
			event_type = info[2]
			event_type2 = info[3]
			counter = info[4][:-2]
			if event_type2 == 'C_CL':
				counter_copy_color = counter
			elif event_type2 == 'C_BW':
				counter_copy_bw = counter
			global_counter = int(counter_copy_color) + int(counter_copy_bw)
			events.append(info)

		print "Events -> ", events
		counter_color_total = int(counter_copy_color) + int(counter_print_color)
		counter_bw_total = int(counter_copy_bw) + int(counter_print_bw)
		log = Log(global_counter, counter_print_bw, counter_print_color, counter_copy_bw, counter_copy_color, counter_color_total, counter_bw_total, printer_id)
		log.upload()

