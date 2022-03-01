from re import I
from django.db import models
from django.utils import timezone

from user.models import Account

CHOICES =[     
    ("avg_heartbeat", 'AVG_HEARTBEAT'),
    ("calories_consumed", 'CALORIES_CONSUMED'),
    ("sleep_hours", 'SLEEP_HOURS'),
    ("morning_pulse", 'MORNING_PULSE')
]

class MetricsData(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_type=models.CharField(max_length=100, choices=CHOICES)
    date = models.DateField(default=timezone.now)
    value = models.FloatField()
