from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict

from .models import Subject, Note
from .forms import NoteForm


def subject_list(request):
    subjects = Subject.objects.all()

    return render(request, 'subject_list.html', {'subjects': subjects})


def note_list(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    notes = subject.note_set.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('note_list', args=(subject_id,)))
    else:
        form = NoteForm(initial={'subject': subject})

    return render(request, 'note_list.html', {'notes': notes, 'subject': subject, 'form': form})


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    subject_id = note.subject.id
    note.delete()

    return HttpResponseRedirect(reverse('note_list', args=(subject_id,)))


def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    subject = note.subject

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('note_list', args=(subject.id,)))
    else:
        form = NoteForm(initial=model_to_dict(note))

    return render(request, 'update_note.html', {'note': note, 'subject': subject, 'form': form})
