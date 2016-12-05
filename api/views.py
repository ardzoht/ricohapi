from django.shortcuts import render
import rest_framework_filters as filters
from api.models import PrinterLog as Logs
from api.serializers import PrinterLogSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.views.generic import ListView, TemplateView
import datetime

from rest_framework import routers, serializers
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

# Create your views here.
class LogDateFilter(filters.FilterSet):
    timestamp = filters.DateTimeFilter(name="timestamp", lookup_type="gte")
    coordinate_X = filters.NumberFilter(name = "coordinate_X")
    coordinate_Y = filters.NumberFilter(name = "coordinate_Y")

    class Meta:
        model = Logs
        fields = ['timestamp', 'coordinate_X', 'coordinate_Y']

class PrinterLog(viewsets.ModelViewSet):
    serializer_class = PrinterLogSerializer
    queryset = Logs.objects.all()
    filter_class = LogDateFilter
