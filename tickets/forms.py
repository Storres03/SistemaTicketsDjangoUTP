from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    """
    Formulario para crear un nuevo ticket. Utiliza widgets personalizados
    para mejorar la presentación de los campos.
    """

    class Meta:
        model = Ticket
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Título del ticket'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Describe el problema',
                'rows': 4
            }),
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
        }
