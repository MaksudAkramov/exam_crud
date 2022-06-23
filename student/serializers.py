from rest_framework import serializers
from rest_framework_simplejwt import serializers as jwt_serializers

from student.models import Student

class StudentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        user = Student.objects.create_user(**validated_data)
        return user

    class Meta:
        
        model = Student
        fields = ['id', 'frist_name', 'last_name', 'faculty']
