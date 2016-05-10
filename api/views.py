from django.shortcuts import render
from api.serializers import PrinterSerializer, PrinterLogSerializer
from api.models import Printer, PrinterLog
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets

# Create your views here.
class PrinterLog(viewsets.ModelViewSet):
	queryset = PrinterLog.objects.all()
	serializer_class = PrinterLogSerializer

class Printers(viewsets.ModelViewSet):
	queryset = Printer.objects.all()
	serializer_class = PrinterSerializer
