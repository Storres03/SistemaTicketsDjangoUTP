from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    # Página principal: lista y creación de tickets
    path('', views.ticket_list, name='list'),
    # Acción para marcar un ticket como atendido
    path('attend/<int:pk>/', views.attend_ticket, name='attend'),
]
