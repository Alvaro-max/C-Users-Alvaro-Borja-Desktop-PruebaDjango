from django import forms
from django.core.exceptions import ValidationError
from admin_contactos.models import Contactos

class formContactos(forms.ModelForm):
    
    nombre = forms.CharField(label="Nombres", widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(max_length=250, label="Email", widget=forms.EmailInput(attrs={"class":"form-control"}))
    numeroCelular = forms.CharField(label="Número de Telefono", widget=forms.TextInput(attrs={"class":"form-control"})) 
    imagenContacto = forms.ImageField(label="Añadir Foto", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))

    def clean_numeroCelular(self):
        numeroCelular = self.cleaned_data['numeroCelular']
        existe = Contactos.objects.filter(numeroCelular = numeroCelular).exists()
        if existe:
            raise ValidationError('Este número ya Existe')
        return numeroCelular



    class Meta:
        model = Contactos
        fields = ('nombre', 'apellido', 'correo', 'numeroCelular', 'imagenContacto')
