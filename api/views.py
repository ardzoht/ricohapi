from django.shortcuts import render
from api.serializers import PrinterSerializer, PrinterLogSerializer, UserSerializer
from api.models import Printer, User
from api.models import PrinterLog as Logs
from api.serializers import PrinterSerializer, PrinterLogSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from django.views.generic import ListView
import datetime
# Create your views here.
class PrinterLog(viewsets.ModelViewSet):
	queryset = Logs.objects.all()
	serializer_class = PrinterLogSerializer

class Printers(viewsets.ModelViewSet):
	queryset = Printer.objects.all()
	serializer_class = PrinterSerializer

class User(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class Dashboard(ListView):
    template_name = "printerlog_list.html"

    def get_queryset(self):
        if self.request.method == 'GET' and 'q' in self.request.GET:
            q = self.request.GET['q']
            option = self.request.GET['dropdown']
            if q:
                if option == 'log':
                    try:
                        return Logs.objects.filter(log_id=q)
                    except ValueError:
                        return Logs.objects.filter(log_id=None)
                elif option == 'date':
                    q=q.split('-')
                    return Logs.objects.filter(timestamp__year=q[0], timestamp__month=q[1], timestamp__day=q[2])
                elif option == 'printer':
                    return Logs.objects.filter(fk_printer=q)
                elif option == 'client';
                    return Logs.objects.filter(fk_printer__client=q)
            else:
                    return Logs.objects.order_by('timestamp')
        else:
            return Logs.objects.order_by('timestamp')

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
