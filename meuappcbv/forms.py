from django import forms
form .models import ViaCep

class ViaCepForm(form.ModelForm):
    class Meta:
        model = ViaCep
        fields = ['cep']
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': 'Digite o CEP','class': 'form-control'}),
        }
        label = {
            'cep': 'CEP'
        }