from django.db import models
from django.contrib.auth.models import User

class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=200)
    hours_spent = models.FloatField()
    mood = models.IntegerField()  # 1-5 scale
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.task} ({self.date})"
    
class Insight(models.Model):
    category = models.CharField(max_length=100)
    value = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category} ({self.value})"
    