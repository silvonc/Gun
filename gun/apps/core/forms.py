from django import forms
from .models import Company, Contact

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Companie'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Companie'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'company', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Contact'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numar Telefon'}),
        }
