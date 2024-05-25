from django import forms
from .models import  User,Poste

class userfrom(forms.ModelForm):
  class Meta:
        model = User
        fields = '__all__'



class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['type', 'date', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'type': forms.Select(choices=Poste.TYPE_CHOICES),
        }









