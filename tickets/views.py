from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

from .models import Ticket
from .forms import TicketForm

@login_required
def ticket_list(request):
    """
    Muestra la lista de tickets y gestiona su creación en función del grupo del usuario.
    - Usuarios en el grupo 'clients' pueden crear tickets y ver solo los suyos.
    - Usuarios en el grupo 'userTec' no pueden crear tickets y ven todos los tickets.
    """
    # Comprobar pertenencia a grupos
    is_client = request.user.groups.filter(name='clients').exists()
    is_userTec = request.user.groups.filter(name='userTec').exists()

    # Filtrar tickets: los clientes solo ven los propios; los técnicos ven todos
    if is_client:
        tickets = Ticket.objects.filter(created_by=request.user)
    else:
        tickets = Ticket.objects.all()

    # Formulario de creación solo para clientes
    form = None
    if is_client:
        form = TicketForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect(reverse('tickets:list'))

    context = {
        'tickets': tickets,
        'form': form,
        'is_client': is_client,
        'is_userTec': is_userTec,
    }
    return render(request, 'tickets/index.html', context)

@login_required
def attend_ticket(request, pk):
    """
    Marca un ticket como atendido asignándolo al usuario actual.
    Solo los usuarios del grupo 'userTec' pueden ejecutar esta acción.
    """
    # Verificar que el usuario sea técnico
    if not request.user.groups.filter(name='userTec').exists():
        return HttpResponseForbidden("No tienes permiso para atender tickets.")

    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.status = 'atendido'
    ticket.assigned_to = request.user
    ticket.save()
    return redirect(reverse('tickets:list'))
