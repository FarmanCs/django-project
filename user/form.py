from django import forms
from .models import UserProfile


class SubjectForm(forms.Form):

    user_subject = forms.ModelChoiceField(
        queryset=UserProfile.objects.select_related("user").all(),
        label="Select student",
        empty_label="Choose a student",
    )
