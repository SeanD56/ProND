from django import forms
from .models import Session, SessionMessage


class SessionForm(forms.ModelForm): # form for creating/editing sessions - all fields except host, which is autoset in views
    class Meta:
        model = Session
        fields = ['skill', 'title', 'description', 'location', 'date_time', 'duration_minutes', 'capacity']
        widgets = {
            'skill': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control', 'min': '5'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }
        labels = {
            'duration_minutes': 'Duration (minutes)', # better label for duration field - decided to use minutes, happy to change
        }


class SessionMessageForm(forms.ModelForm):
    class Meta:
        model = SessionMessage
        fields = ['content', 'is_announcement']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Write a message to the session...',
            }),
            'is_announcement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'content': 'Message',
            'is_announcement': 'Post as host announcement',
        }


class SessionMessageEditForm(forms.ModelForm):
    class Meta:
        model = SessionMessage
        fields = ['content', 'is_announcement']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
            }),
            'is_announcement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'content': 'Message',
            'is_announcement': 'Keep as host announcement',
        }
