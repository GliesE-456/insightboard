from rest_framework import viewsets
from .models import DailyLog, Insight
from .serializers import DailyLogSerializer, InsightSerializer
from django.http import JsonResponse


def insights(request):
    data = [
        {"id": 1, "category": "Performance", "value": 78},
        {"id": 2, "category": "Engagement", "value": 65},
        {"id": 3, "category": "Growth", "value": 90},
    ]
    return JsonResponse(data, safe=False)


class DailyLogViewSet(viewsets.ModelViewSet):
    queryset = DailyLog.objects.all().order_by('-date')
    serializer_class = DailyLogSerializer
    filterset_fields = ['user', 'mood', 'date']
    search_fields = ['task', 'notes']

class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all()
    serializer_class = InsightSerializer