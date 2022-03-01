from rest_framework import serializers
from metricdatapoint import models

class SpesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MetricsData
        fields = ['date', 'value']     

class MetricsDataPointSerializer(serializers.ModelSerializer):
    x_data_type = serializers.ChoiceField(choices=models.CHOICES)
    y_data_type = serializers.ChoiceField(choices=models.CHOICES)
    x = SpesDataSerializer(many=True)
    y = SpesDataSerializer(many=True)
    
    class Meta:
        model = models.MetricsData
        fields = ['x_data_type', 'y_data_type', 'x', 'y']
             
class DataSerializer(serializers.ModelSerializer):

    data = MetricsDataPointSerializer()

    class Meta:
        
        model = models.MetricsData
        fields = ['user_id', 'data']
    
    def create(self, validated_data):
        for object in validated_data['data']['x']:
            if models.MetricsData.objects.filter(
                user_id=validated_data['user_id'],
                data_type=validated_data['data']['x_data_type'],
                date=object['date']):
                    models.MetricsData.objects.filter(
                        user_id=validated_data['user_id'],
                        data_type=validated_data['data']['x_data_type'],
                        date=object['date']).update(value=object['value'])
            else:
                models.MetricsData.objects.create(
                                user_id=validated_data['user_id'],
                                data_type=validated_data['data']['x_data_type'],
                                date=object['date'],
                                value=object['value'])

        for object in validated_data['data']['y']:
            if models.MetricsData.objects.filter(
                                user_id=validated_data['user_id'],
                                data_type=validated_data['data']['y_data_type'],
                                date=object['date']
            ):
                models.MetricsData.objects.filter(
                                user_id=validated_data['user_id'],
                                data_type=validated_data['data']['y_data_type'],
                                date=object['date']).update(value=object['value'])
            else:
                models.MetricsData.objects.create(
                                user_id=validated_data['user_id'],
                                data_type=validated_data['data']['y_data_type'],
                                date=object['date'],
                                value=object['value'])

        return validated_data
