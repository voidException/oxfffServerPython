from cmdb import models
from rest_framework import serializers

class IDCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IDC
        fields = ('name',)

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Host
        fields = ('id','hostname','ip_addr','port','idc','system_type','memo','enabled')