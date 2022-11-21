from django import forms
from t_test_app.models import UserEntries


class NewEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntries
        fields = '__all__'
