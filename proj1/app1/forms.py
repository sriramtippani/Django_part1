from django import forms
from app1.models import Job1Model

class Job1Form(forms.ModelForm):
    def clean_age(self):
        input_age = self.cleaned_data['Age']
        if input_age < 20:
            raise forms.ValidationError('The minimum age should be above 20')
        return input_age

    class Meta:
        model = Job1Model
        fields = '__all__'