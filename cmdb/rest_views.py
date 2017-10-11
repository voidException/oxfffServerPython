from rest_framework import viewsets
from cmdb import models
from cmdb import rest_serializer



class IDCViewSet(viewsets.ModelViewSet):
    queryset = models.IDC.objects.all()
    serializer_class = rest_serializer.IDCSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = models.Host.objects.all()
    serializer_class = rest_serializer.HostSerializer