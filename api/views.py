from django.shortcuts import render
from api.models import Printer
from api.models import PrinterLog as Logs
from api.serializers import PrinterSerializer, PrinterLogSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from django.views.generic import ListView, TemplateView
import datetime
# Create your views here.
class PrinterLog(viewsets.ModelViewSet):
	queryset = Logs.objects.all()
	serializer_class = PrinterLogSerializer

class Printers(viewsets.ModelViewSet):
	queryset = Printer.objects.all()
	serializer_class = PrinterSerializer

class Dashboard(TemplateView):
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['clients'] = Printer.objects.values("client").distinct()
        return context

class Log(ListView):
    template_name = "printerlog_list.html"
    total_list = None

    def get_queryset(self):
        if self.request.method == 'GET' and 'q' in self.request.GET:
            q = self.request.GET['q']
            check = self.request.GET.get('cut', False)
            if q and 'dropdown' in self.request.GET:
                option = self.request.GET['dropdown']
                if option == 'date':
                    q=q.split('-')
                    date_list = Logs.objects.filter(timestamp__year=q[0], timestamp__month=q[1], timestamp__day=q[2])
                    return date_list
                elif option == 'printer':
                    printer_list = Logs.objects.filter(fk_printer=q).order_by("timestamp")
                    if check == 'check' :
                        printer_list =  self.get_cut_date(printer_list, q, option)
                    self.total_list = printer_list
                    return printer_list
                elif option == 'client' :
                    client_list = Logs.objects.filter(fk_printer__client=q).order_by("timestamp")
                    if check == 'check' :
                        client_list = self.get_cut_date(client_list, q, option)
                    return client_list
            else:
                client_list = Logs.objects.filter(fk_printer__client=q).order_by("timestamp")
                if check == 'check' :
                    client_list = self.get_cut_date(client_list, q, 'client')
                return client_list
        else:
            return Logs.objects.order_by('timestamp')

    def get_cut_date(self, queryset, q, option):
        if option == 'client':
            latest = Printer.objects.filter(client = q).latest('cutDate')
        else:
            latest = Printer.objects.filter(printer_id = q).latest('cutDate')
        now = datetime.datetime.now()
        return queryset.filter(timestamp__day__lte=latest.cutDate, timestamp__month=now.month)

    def get_context_data(self, **kwargs):
        context = super(Log, self).get_context_data(**kwargs)
        if self.total_list:
          total = {}
          earliest = self.total_list.values("counter_print_color", "counter_print_bw", 
            "counter_copy_color", "counter_copy_bw", "counter_color_total", "counter_bw_total",
             "counter_toner_yellow", "counter_toner_cyan", "counter_toner_black", 
            "counter_toner_magenta").earliest("timestamp")

          latest = self.total_list.values("counter_print_color", "counter_print_bw", 
            "counter_copy_color", "counter_copy_bw", "counter_color_total", "counter_bw_total",
             "counter_toner_yellow", "counter_toner_cyan", "counter_toner_black", 
            "counter_toner_magenta").latest("timestamp")
          for key in latest:
              total[key] = latest[key] - earliest[key]
          context["total"] = total
          return context
        return context;


class Connection(ListView):
    template_name="printerid_list.html"
    model = Printer

    def get_context_data(self, **kwargs):
        connection = []
        context = super(Connection, self).get_context_data(**kwargs)
        for printer in Printer.objects.all():
            now = datetime.datetime.now()
            now_minus_5 = now - datetime.timedelta(minutes=5)
            timestamp = Logs.objects.filter(timestamp__day=now.day)
            if now_minus_5 != timestamp:
                connection.append("not connected")
            else:
                connection.append("connected")
        connection.reverse()
        context["connected"] = connection
        return context
