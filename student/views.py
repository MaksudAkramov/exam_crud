from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import serializers
from rest_framework import status



@api_view(['GET'])
def view_student(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        student = Student.objects.filter(**request.query_param.dict())
    else:
        student = Student.objects.all()
  
    # if there is something in student else raise error
    if student:
        data = StudentSerializer(student)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['POST'])
def add_student(request):
    item = StudentSerializer(data=request.data)
  
    # validating for already existing data
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_student(request, pk):
    item = Student.objects.get(pk=pk)
    data = Student(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Student, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)