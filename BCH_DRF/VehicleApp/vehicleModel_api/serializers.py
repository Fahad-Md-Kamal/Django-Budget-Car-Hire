from rest_framework import serializers

from AppUsers.serializers import UserListSerializer
from CoreApp.models import VehicleModel


class VehicleModelSerializer(serializers.HyperlinkedModelSerializer):
    created_by              = UserListSerializer(read_only=True)
    updated_by              = UserListSerializer(read_only=True)
    updated_on              = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model               = VehicleModel
        fields              = ( 'id',
                                'url',  
                                'name', 
                                'description', 
                                'created_on', 
                                'created_by',  
                                'updated_on',
                                'updated_by',)


class VehicleModelListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model               = VehicleModel
        fields              = ('url', 'name')
