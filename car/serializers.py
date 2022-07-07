from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_serializers

from student.models import Student

class CarSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        car_object = Car.objects.create_user(**validated_data)
        return car_object

    class Meta:
        
        model = Car
        fields = ['id', 'manufacturer', 'model', 'year_of_manufacturing']
