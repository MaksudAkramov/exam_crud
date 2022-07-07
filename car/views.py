from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from car.models import Car
from car.serializers import CarSerializer
from rest_framework import serializers
from rest_framework import status



@api_view(['GET'])
def view_car(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        car = Car().objects.filter(**request.query_param.dict())
    else:
        car = Car().objects.all()
  
    # if there is something in student else raise error
    if car:
        data = CarSerializer(car)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['POST'])
def add_car(request):
    item = CarSerializer(data=request.data)
  
    # validating for already existing data
    if Car().objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_car(request, pk):
    item = Car().objects.get(pk=pk)
    data = Car()(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_car(request, pk):
    item = get_object_or_404(Car(), pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)