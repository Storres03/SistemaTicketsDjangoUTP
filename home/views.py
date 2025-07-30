# home/views.py
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    return render(request, 'home/index.html')

def logout_view(request):
    """
    Finaliza la sesión del usuario y lo redirige a la página de inicio.
    Acepta solicitudes GET y POST para facilitar el enlace desde plantillas.
    """
    logout(request)
    return redirect('index')