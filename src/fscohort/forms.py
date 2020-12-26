from django import forms
from .models import Student # Bu satir ilk form yazim ornegi icin gerekli degil

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 50, label='Your name')
    last_name = forms.CharField(max_length = 50, label='Your surname')
    number = forms.IntegerField()

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__' # Butun sutun adlarini otomatik getirir