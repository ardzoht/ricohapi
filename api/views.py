from django.shortcuts import render
import rest_framework_filters as filters
from api.models import Printer
from api.models import PrinterLog as Logs
from api.serializers import PrinterSerializer, PrinterLogSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets #  filters
from rest_framework.renderers import JSONRenderer
from django.views.generic import ListView, TemplateView
import datetime

from rest_framework import routers, serializers
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

# Create your views here.
class LogDateFilter(filters.FilterSet):
    timestamp = filters.DateTimeFilter(name="timestamp", lookup_type="gte")

    class Meta:
        model = Logs
        fields = ['timestamp']

class PrinterFilters(filters.FilterSet):
    printer_id = filters.CharFilter(name = "printer_id")
    client = filters.CharFilter(name = "client")
    cutDate = filters.NumberFilter(name = "cutDate")

    class Meta:
        model = Printer
        fields = ['printer_id', 'client', 'cutDate']

class PrinterLog(viewsets.ModelViewSet):
    serializer_class = PrinterLogSerializer
    queryset = Logs.objects.all()
    filter_class = LogDateFilter


class Printers(viewsets.ModelViewSet):
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()
    filter_class = PrinterFilters

class Dashboard(TemplateView):
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['clients'] = Printer.objects.values("client").distinct()
        return context

class Log(ListView):
    template_name = "printerlog_list.html"
    total_list = None
    total = False

    def get_queryset(self):
        if self.request.method == 'GET' and 'q' in self.request.GET:
            q = self.request.GET['q']
            check = self.request.GET.get('cut', False)
            total = self.request.GET.get('total', False)

            if q and 'dropdown' in self.request.GET:
                option = self.request.GET['dropdown']
                if option == 'date':
                    q=q.split('-')
                    date_list = Logs.objects.filter(timestamp__year=q[0], timestamp__month=q[1], timestamp__day=q[2])
                    self.total_list = date_list
                    return date_list
                elif option == 'printer':
                    printer_list = Logs.objects.filter(fk_printer=q).order_by("timestamp")
                    if check == 'check' :
                        printer_list =  self.get_cut_date(printer_list, q, option)
                    self.total_list = printer_list
                    return printer_list
                elif option == 'client' :
                    self.total = True
                    client_list = Logs.objects.filter(fk_printer__client=q).order_by("timestamp")
                    if check == 'check' :
                        client_list = self.get_cut_date(client_list, q, option)
                    self.total_list = client_list
                    return 
            else:
                client_list = Logs.objects.filter(fk_printer__client=q).order_by("timestamp")
                if check == 'check' :
                    client_list = self.get_cut_date(client_list, q, 'client')
                self.total_list = client_list
                if total == 'total':
                    self.total = True
                    return
                return client_list
        else:
            return Logs.objects.last('timestamp')[:10]

    def get_cut_date(self, queryset, q, option):
        if option == 'client':
            latest = Printer.objects.filter(client = q).latest('cutDate')
        else:
            latest = Printer.objects.filter(printer_id = q).latest('cutDate')
        now = datetime.datetime.now()
        first = now.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        return queryset.filter(timestamp__gte=datetime.date(lastMonth.year, lastMonth.month, latest.cutDate), timestamp__lte=datetime.date(now.year, now.month, latest.cutDate))

    def get_logs_values(self, total_list, id):
        return total_list.filter(fk_printer=id).values("fk_printer", "counter_print_color", "counter_print_bw", 
                      "counter_copy_color", "counter_copy_bw", "counter_color_total", "counter_bw_total",
                       "counter_toner_yellow", "counter_toner_cyan", "counter_toner_black", 
                      "counter_toner_magenta", "timestamp")

    def get_last_ten_logs_values(self, total_list, id):
        return total_list.filter(fk_printer=id).values("fk_printer", "counter_print_color", "counter_print_bw", 
                      "counter_copy_color", "counter_copy_bw", "counter_color_total", "counter_bw_total",
                       "counter_toner_yellow", "counter_toner_cyan", "counter_toner_black", 
                      "counter_toner_magenta", "timestamp").reverse()[:10]

    def get_context_data(self, **kwargs):
        context = super(Log, self).get_context_data(**kwargs)
        if self.total_list:
            printer_list = []
            ids = self.total_list.order_by('fk_printer').values_list('fk_printer').distinct()
            total = {"counter_print_color": 0, "counter_print_bw":0, 
                  "counter_copy_color":0, "counter_copy_bw":0, "counter_color_total":0, "counter_bw_total":0,
                   "counter_toner_yellow":0, "counter_toner_cyan":0, "counter_toner_black":0, 
                  "counter_toner_magenta":0}
            for id in ids:  
                total_id = {}
                earliest = self.get_logs_values(self.total_list, id).earliest("timestamp")
                latest = self.get_logs_values(self.total_list, id).latest("timestamp")
                print(latest['timestamp'])
                total_id["fk_printer"] = latest["fk_printer"]
                for key in latest:
                    if key != "fk_printer" and key != "timestamp":
                        total_id[key] = latest[key] - earliest[key]
                        total[key] += total_id[key]
                if self.total:
                    total_id["logs"] = self.get_last_ten_logs_values(self.total_list, id)
                    printer_list.append(total_id)
            context['total_printer'] = printer_list
            context['total'] = total 
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
