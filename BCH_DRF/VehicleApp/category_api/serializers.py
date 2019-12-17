from rest_framework import serializers

from AppUsers.serializers import UserListSerializer
from CoreApp.models import VehicleCategory


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    updated_by          = UserListSerializer(read_only=True)
    created_by          = UserListSerializer(read_only=True)

    class Meta:
        model           = VehicleCategory
        fields          = ( 'id',
                            'url',
                            'name',
                            'description', 
                            'created_on',
                            'updated_on',
                            'created_by',
                            'updated_by')
                            

class CategoryListSerializer(CategoryDetailSerializer):

    class Meta:
        model           = VehicleCategory
        fields          = ( 'url',
                            'name',)
                            