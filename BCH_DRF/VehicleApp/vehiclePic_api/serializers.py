from rest_framework import serializers

from CoreApp.models import VehiclePics


class VehiclePictureUploadSerializer(serializers.HyperlinkedModelSerializer):
    booked_date             = serializers.ReadOnlyField(read_only=True)
    is_approved             = serializers.ReadOnlyField(read_only=True) 
    
    class Meta:
        model               = VehiclePics
        fields              = ( 'url', 
                                'booked_date', 
                                'image', 
                                'is_main', 
                                'is_approved', 
                                'timestamp', 
                                'vehicle')

    def validate(self, data):
        request             = self.context.get('request')
        requested_user      = request.user
        vehicle             = data.get('vehicle')

        if requested_user != vehicle.user:
            raise serializers.ValidationError('You have no right to perform this action.')

        if VehiclePics.objects.filter(vehicle=vehicle).count() >= 5:
            raise serializers.ValidationError('This vehicle has Five pictures already')
        
        return data



class VehiclePictureSerializer(VehiclePictureUploadSerializer):

    class Meta:
        model               = VehiclePics
        fields              = ( 'url', 
                                'booked_date', 
                                'image', 
                                'is_main',)

