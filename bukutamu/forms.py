from django import forms
from django.forms import widgets
from .models import BukuTamu

class FormBukuTamu(forms.ModelForm):
    class Meta:
        model = BukuTamu
        fields = ('nama', 'alamat', 'telepon', 'email', 'instansi', 'tanggal', 'keperluan', 'keperluan_lainnya')
        
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'telepon': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'instansi': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'tanggal': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'keperluan': forms.Select(
                attrs={'class': "form-control", 'id': "select_status", 'type': "text", 'required': ""}),
            'keperluan_lainnya': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
        }