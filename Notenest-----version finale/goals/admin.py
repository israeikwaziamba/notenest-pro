from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'deadline', 'completed')
    list_filter = ('completed', 'deadline')
    search_fields = ('title',)

admin.site.register(Goal, GoalAdmin)