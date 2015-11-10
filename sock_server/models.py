import json
import requests

class Log:

	def __init__(self, message=None):
		#define message slicing by protocol structure

		# Using dummy data for now
		self.global_counter = 10
		self.counter_print_bw = 4
		self.counter_print_color = 0
		self.counter_copy_bw  = 4
		self.counter_copy_color = 2
		self.fk_printer = 0

	def to_json(self):
		return json.dumps(self, default= lambda o: o.__dict__, sort_keys=True, indent=4)

	def upload(self):
		headers = {'Content-Type': "application/json"}
		r = requests.post("http://riego.chi.itesm.mx:8081/api/logs/", data=self.to_json(), 
        				  headers=headers)
		print self.to_json(), r.raise_for_status()

