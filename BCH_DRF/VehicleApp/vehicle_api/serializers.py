from rest_framework import serializers

from CoreApp.models import Vehicle, VehiclePics
from AppUsers.serializers import UserListSerializer
from VehicleApp.category_api.serializers import CategoryListSerializer
from VehicleApp.vehicleModel_api.serializers import VehicleModelListSerializer
from VehicleApp.vehiclePic_api.serializers import VehiclePictureSerializer


class ADMINVehicleSerializer(serializers.HyperlinkedModelSerializer):
    owner                       = UserListSerializer(read_only=True, label= 'Vehicle Owner')
    updated_by                  = UserListSerializer(read_only=True)
    booked_date                 = serializers.ReadOnlyField(read_only=True)
    updated_on                  = serializers.ReadOnlyField(read_only=True)
    vehicle_category            = serializers.SerializerMethodField(read_only=True)
    vehicle_model               = serializers.SerializerMethodField(read_only=True)
    vehicle_image               = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model                   = Vehicle
        fields                  = ( 'url',
                                    'registration_no',
                                    'registared_on',
                                    'rent',        
                                    'capacity',        
                                    'is_blocked',
                                    'is_approved', 
                                    'is_booked', 
                                    'is_hired', 
                                    'booked_date', 
                                    'owner',                    
                                    'model', 
                                    'category', 
                                    'vehicle_model', 
                                    'vehicle_category', 
                                    'updated_on',              
                                    'updated_by',
                                    'vehicle_image' )
    
    def get_vehicle_category(self, data):
        return data.category.name
    

    def get_vehicle_model(self, data):
        return data.model.name
    

    def get_vehicle_image(self, obj):
        request             = self.context.get('request')
        qs                  = VehiclePics.objects.filter(vehicle=obj).order_by('is_main')
        return VehiclePictureSerializer(qs, many=True, context={'request':request}).data




class VehicleSerializer(ADMINVehicleSerializer):
    class Meta:
        model                   = Vehicle
        fields                  = ( 'url',
                                    'registration_no',
                                    'vehicle_model',  
                                    'vehicle_category',
                                    'registared_on',
                                    'rent',        
                                    'capacity',        
                                    'is_blocked',
                                    'is_approved', 
                                    'is_booked', 
                                    'is_hired', 
                                    'booked_date', 
                                    'owner',                    
                                    'model', 
                                    'category',
                                    'vehicle_image')

        read_only_fields        = ( 'is_blocked',
                                    'is_approved',
                                    'is_booked',
                                    'is_hired',)


class VehicleListSerializer(ADMINVehicleSerializer):
    
    class Meta:
        model                   = Vehicle
        fields                  = ( 'url',
                                    'registration_no',
                                    'vehicle_model',  
                                    'vehicle_category',
                                    'registared_on',
                                    'rent',        
                                    'capacity',
                                    'vehicle_image')

        read_only_fields        = ( 'is_blocked',
                                    'is_approved',
                                    'is_booked',
                                    'is_hired',)


    def get_vehicle_image(self, obj):
        request             = self.context.get('request')
        qs                  = VehiclePics.objects.filter(vehicle=obj, is_main=True, is_approved=True)
        return VehiclePictureSerializer(qs, many=True, context={'request':request}).data



class VehiclePublicSerializer(VehicleListSerializer):
    vehicle_image               = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model                   = Vehicle
        fields                  = ( 'url',
                                    'vehicle_model',  
                                    'vehicle_category',
                                    'rent',        
                                    'capacity',
                                    'vehicle_image')



