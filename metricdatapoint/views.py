from rest_framework.response import Response
from rest_framework import viewsets,status

from metricdatapoint.models import MetricsData
from metricdatapoint.permissions import MetricPermission
from metricdatapoint.serializers import DataSerializer



class MatricDataViewset(viewsets.ModelViewSet):
    queryset = MetricsData.objects.all()
    serializer_class = DataSerializer

    permission_classes = [MetricPermission]

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)