from rest_framework import serializers
from .models import ActivityPeriod

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'