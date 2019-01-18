from django import forms
from .models import Note, Subject


class NoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-3', 'placeholder': 'Note Title'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mx-3', 'placeholder': 'Note Text'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Note
        fields = ['title', 'text', 'subject']

