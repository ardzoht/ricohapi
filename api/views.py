from django.shortcuts import render
from api.serializers import PrinterSerializer, UserSerializer
from api.models import Printer, User
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets

# Create your views here.
class PrinterList(ListCreateAPIView):
	queryset = Printer.objects.all()
	serializer_class = PrinterSerializer
	paginate_by = 10

class Printers(viewsets.ModelViewSet):
	queryset = Printer.objects.all()
	serializer_class = PrinterSerializer

class User(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer