from rest_framework.serializers import ModelSerializer

from .models import WorldData, Variable

class WorldDataSerializer(ModelSerializer):
    class Meta:
        model   = WorldData
        fields  = '__all__'

class VariableSerializer(ModelSerializer):
    class Meta:
        model   = Variable
        fields  = '__all__'