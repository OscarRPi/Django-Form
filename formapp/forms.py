#forms.py

from django import forms  
from formapp.models import Data_User

class DataForm(forms.ModelForm):  
    class Meta:  
        model = Data_User  
        fields = ['id_usuario', 'nombres', 'apellidos', 'correo', 'ciudad'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 
            'nombres':  forms.TextInput (attrs={ 'class': 'form-control' }), 
            'apellidos':forms.TextInput (attrs={ 'class': 'form-control' }),
            'correo':   forms.EmailInput(attrs={ 'class': 'form-control' }),
            'ciudad':   forms.TextInput (attrs={ 'class': 'form-control' }),
        }