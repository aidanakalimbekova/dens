# Create your views here.

from django.shortcuts import render
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer
from rest_framework import viewsets

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()