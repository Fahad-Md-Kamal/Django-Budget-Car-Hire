from rest_framework import serializers
from uuid import uuid4

from CoreApp.models import Fleet, Vehicle


from AppUsers.serializers import UserListSerializer
from VehicleApp.vehicle_api.serializers import VehicleListSerializer, VehiclePublicSerializer

class FleetDetailSerializers(serializers.ModelSerializer):
    fleet_ref               = serializers.ReadOnlyField(read_only=True)
    approved_on             = serializers.ReadOnlyField(read_only=True)
    user                    = UserListSerializer(read_only=True)
    fleet_info              = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model               = Fleet
        fields              = ( 'url', 
                                'fleet_ref', 
                                'booked_date', 
                                'is_purchased', 
                                'is_approved', 
                                'is_freezed', 
                                'approved_on', 
                                'user',
                                'vehicle',
                                'fleet_info',
                                )

        read_only_fields    = ( 'is_purchased', 
                                'is_approved', 
                                'is_freezed', )


    def get_fleet_info(self, obj):
        request                 = self.context.get('request')
        data                    = {
            'total_vehicle': obj.vehicle.count(),
            'total_rent': obj.get_total(),
            'vehicle': VehiclePublicSerializer(obj.vehicle, many=True, context={'request':request} ).data,
        }
        return data  


class FleetListSerializers(FleetDetailSerializers):

    class Meta:
        model               = Fleet
        fields              = ( 'url', 
                                'fleet_ref', 
                                'booked_date', 
                                'is_purchased', 
                                'is_approved', 
                                'is_freezed', 
                                'approved_on', 
                                'user', 
                                'fleet_info',)


class FleetCreateSerializers(FleetDetailSerializers):

    class Meta:
        model               = Fleet
        fields              = ( 'url', 
                                'fleet_ref', 
                                'booked_date', 
                                'is_purchased', 
                                'is_approved', 
                                'is_freezed', 
                                'approved_on', 
                                'user',
                                'vehicle',
                                'fleet_info', )

        read_only_fields    = ( 'is_purchased', 
                                'is_approved', 
                                'is_freezed', )
    

    def create(self, validated_data):
        request             = self.context.get('request')
        user                = request.user
        rf_id = (user.username[:3] + '-' + str(uuid4())[-6:]).upper()
        obj = Fleet(fleet_ref = rf_id) 
        obj.save()
        obj.vehicle.set(validated_data.get('vehicle'))
        obj.set_booked()
        obj.save()
        return obj
    

    # def update(self, instance, validated_data):
    #     fleet           = Fleet.objects.filter(id = instance.id)
    #     print(fleet)
    #     fleet.vehicle.set(validated_data.get('vehicle'))
    #     fleet.set_booked()
    #     fleet.save()
    #     return instance 