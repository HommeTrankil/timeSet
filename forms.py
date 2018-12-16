from django import forms

from .models import sugarTest

class MyTaskForm(forms.ModelForm):
    class Meta:
       model = sugarTest
       fields = ('name','phone','email','service','holiday_date','contact_time','comment')

