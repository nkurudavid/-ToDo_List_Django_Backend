from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','status','created_date',)
    list_filter = ('status',)
    search_fields = ('title',)
    ordering = ('created_date',)