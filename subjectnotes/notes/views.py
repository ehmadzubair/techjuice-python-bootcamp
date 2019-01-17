from django.shortcuts import render, get_object_or_404
from .models import Subject


def subject_list(request):
    subjects = Subject.objects.all()

    return render(request, 'subject_list.html', {'subjects': subjects})


def note_list(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    notes = subject.note_set.all()

    return render(request, 'note_list.html', {'notes': notes})
