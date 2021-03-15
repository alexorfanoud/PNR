from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg

from .models import WorldData, Variable
from .serializers import WorldDataSerializer, VariableSerializer

class ApiIndexView(APIView):
    def get(self, request, format=None):
        queryset = WorldData.objects.all()
        serializer = WorldDataSerializer(queryset, many=True)
        return Response(serializer.data)

class PKDetailView(APIView):
    def get(self, request, key, format=None):
        queryset = WorldData.objects.filter(pk=key)
        serializer = WorldDataSerializer(queryset, many=True)
        return Response(serializer.data)

class ModelDetailView(APIView):
    def get(self, request, model, format=None):
        queryset = WorldData.objects.filter(model=model)
        serializer = WorldDataSerializer(queryset, many=True)
        return Response(serializer.data)

class ScenarioDetailView(APIView):
    def get(self, request, scenario, format=None):
        queryset = WorldData.objects.filter(scenario=scenario)
        serializer = WorldDataSerializer(queryset, many=True)
        return Response(serializer.data)

class SectorDetailView(APIView):
    def get(self, request, section, format=None):
        queryset = WorldData.objects.filter(variable__section=section)
        serializer = WorldDataSerializer(queryset, many=True)
        return Response(serializer.data)

class AvgByModelAndVariable(APIView):
    def get(self, request, scenario, format=None):
        queryset = WorldData.objects.filter(scenario=scenario)\
            .values('model', 'variable')\
            .annotate(
                Avg('_2005'),
                Avg('_2010'),
                Avg('_2015'),
                Avg('_2020'),
                Avg('_2025'),
                Avg('_2030'),
                Avg('_2035'),
                Avg('_2040'),
                Avg('_2045'),
                Avg('_2050'),
                Avg('_2055'),
                Avg('_2060'),
                Avg('_2065'),
                Avg('_2070'),
                Avg('_2075'),
                Avg('_2080'),
                Avg('_2085'),
                Avg('_2090'),
                Avg('_2095'),
                Avg('_2100'),
                )
        return Response(queryset)