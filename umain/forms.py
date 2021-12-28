from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import *


class AddEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):  # Constructon
        super().__init__(*args, **kwargs)  # Base class constructor
        self.fields['cat'].empty_label = "Select category"

    class Meta:
        model = Event
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length more than 200 symbols')
        return title
