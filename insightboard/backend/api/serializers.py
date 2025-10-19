from rest_framework import serializers
from .models import DailyLog, Insight

class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = '__all__'