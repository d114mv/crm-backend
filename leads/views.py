from rest_framework import viewsets
from .models import Carrera, Lead, Interaccion
from .serializers import CarreraSerializer, LeadSerializer, InteraccionSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by('-fecha_creacion')
    serializer_class = LeadSerializer

class InteraccionViewSet(viewsets.ModelViewSet):
    queryset = Interaccion.objects.all().order_by('-fecha')
    serializer_class = InteraccionSerializer