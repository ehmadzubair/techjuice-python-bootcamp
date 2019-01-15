from django.contrib import admin

# Register your models here.
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'title']

admin.site.register(Subject, SubjectAdmin)