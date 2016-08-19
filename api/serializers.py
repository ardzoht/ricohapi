from rest_framework.serializers import ModelSerializer, IntegerField, ReadOnlyField, CharField
from api.models import Printer, PrinterLog
# Create your views here.

class PrinterSerializer(ModelSerializer):
    class Meta:
        model = Printer
        fields = ('printer_id', 'description', 'emailReport', 'cutDate', 'client')

    def save(self):
        obj = Printer(printer_id = self.validated_data['printer_id'], description = self.validated_data['description'], emailReport = self.validated_data['emailReport'], cutDate = self.validated_data['cutDate'], client = self.validated_data['client'])
        obj.save()

class PrinterLogSerializer(ModelSerializer):
    log_id = ReadOnlyField()
    
    class Meta:
        model = PrinterLog
        fields = ('log_id', 'timestamp', 'global_counter', 'counter_print_bw', 'counter_print_color','counter_copy_bw', 'counter_copy_color','counter_bw_total', 'counter_color_total', 'fk_printer', 'counter_fax_bw', 'counter_fax_color', 'counter_toner_black', 'counter_toner_cyan', 'counter_toner_magenta', 'counter_toner_yellow', 'counter_duplex', 'coordinate_X', 'coordinate_Y')

    def save(self):
        obj = PrinterLog(global_counter = self.validated_data['global_counter'], counter_copy_color = self.validated_data['counter_copy_color'], 
            counter_copy_bw = self.validated_data['counter_copy_bw'], counter_print_color = self.validated_data['counter_print_color'], 
            counter_bw_total = self.validated_data['counter_bw_total'], counter_color_total = self.validated_data['counter_color_total'], 
            counter_print_bw = self.validated_data['counter_print_bw'], fk_printer = self.validated_data['fk_printer'], 
            counter_fax_bw = self.validated_data['counter_fax_bw'], counter_fax_color = self.validated_data['counter_fax_color'], 
            counter_toner_black=self.validated_data['counter_toner_black'], counter_toner_cyan = self.validated_data['counter_toner_cyan'], 
            counter_toner_magenta = self.validated_data['counter_toner_magenta'], counter_toner_yellow = self.validated_data['counter_toner_yellow'], 
            counter_duplex = self.validated_data['counter_duplex'], coordinate_X = self.validated_data['coordinate_X'], coordinate_Y = self.validated_data['coordinate_Y'])
        obj.save()