from django.contrib import admin
from .models import DailyLog, Insight

@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'date', 'hours_spent', 'mood')  # columns shown in list view
    list_filter = ('date', 'mood', 'user')  # filters on the sidebar
    search_fields = ('task', 'notes', 'user__username')  # searchable fields
    ordering = ('-date',)  # latest logs first
    date_hierarchy = 'date'  # add date navigation at the top

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('category', 'value', 'description')
    search_fields = ('category', 'description')
    list_filter = ('category',)  # filter by category
    ordering = ('category',)  # order by category