from django import forms
from app1.models import SriModel

class SriForm(forms.ModelForm):

    def clean_esal(self):
        salary = self.cleaned_data['esal']
        if salary < 30000:
            raise forms.ValidationError('The minimum salary should be 30000')
        return salary

    class Meta:
        model = SriModel
        fields = '__all__'