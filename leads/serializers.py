from rest_framework import serializers
from .models import Carrera, Lead, Interaccion

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class InteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaccion
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    nombre_carrera = serializers.CharField(source='carrera_interes.nombre', read_only=True)

    class Meta:
        model = Lead
        fields = '__all__'