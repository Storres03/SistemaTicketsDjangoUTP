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
    Vista principal de tickets.

    Muestra la lista de tickets existentes y permite crear uno nuevo.
    Solo usuarios autenticados pueden acceder a esta página.
    """
    # Determinar rol del usuario según los grupos
    is_client = request.user.groups.filter(name='clients').exists()
    is_userTec = request.user.groups.filter(name='userTec').exists()

    # Filtrar tickets según rol
    if is_client:
        tickets = Ticket.objects.filter(created_by=request.user)
    else:
        tickets = Ticket.objects.all()

    # Manejo del formulario de creación: solo clientes pueden crear tickets
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
    Marca un ticket como atendido.

    Asigna el ticket al usuario que realiza la acción y actualiza el estado a "atendido".
    """
    # Verificar que el usuario pertenece al grupo userTec
    if not request.user.groups.filter(name='userTec').exists():
        return HttpResponseForbidden("No tienes permiso para atender tickets.")

    ticket = get_object_or_404(Ticket, pk=pk)
    # Actualizar estado y usuario asignado
    ticket.status = 'atendido'
    ticket.assigned_to = request.user
    ticket.save()
    return redirect(reverse('tickets:list'))
