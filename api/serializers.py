from rest_framework.serializers import ModelSerializer, IntegerField, ReadOnlyField, CharField
from api.models import Printer, User, PrinterLog
# Create your views here.

class PrinterSerializer(ModelSerializer):
	class Meta:
		model = Printer
		fields = ('printer_id', 'description')

class UserSerializer(ModelSerializer):

	total_counter = IntegerField(source='user_total_counter')
	print_black_white_counter = IntegerField(source='user_counter_print_bw')
	print_color_counter = IntegerField(source='user_counter_print_color')
	copy_black_white_counter = IntegerField(source='user_counter_copy_bw')
	copy_color_counter = IntegerField(source='user_counter_copy_color')

	class Meta:
		model = User
		fields = ('user_id', 'user_name', 'total_counter', 'print_black_white_counter',
				  'print_color_counter', 'copy_black_white_counter', 'copy_color_counter',
				  'printers')

class PrinterLogSerializer(ModelSerializer):
	log_id = ReadOnlyField()

	class Meta:
		model = PrinterLog
		fields = ('log_id', 'timestamp', 'global_counter', 'counter_print_bw', 'counter_print_color','counter_copy_bw', 'counter_copy_color','counter_bw_total', 'counter_color_total', 'fk_printer')
