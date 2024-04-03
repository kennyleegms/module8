from django import forms

from . import models , widgets

class registration_form(forms.ModelForm):
    class Meta:
        model = models.table
        fields = ["task_name","category","due_date"]
        widgets = {"due_date":widgets.DatePickerInput()}