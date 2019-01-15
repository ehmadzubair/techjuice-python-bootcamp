from django.contrib import admin
from .models import Subject, Note


class SubjectAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'title']


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['id', 'subject', 'title']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Note, NoteAdmin)
