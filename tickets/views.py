from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Ticket
from .forms import TicketForm


@login_required
def ticket_list(request):
    """
    Vista principal de tickets.

    Muestra la lista de tickets existentes y permite crear uno nuevo.
    Solo usuarios autenticados pueden acceder a esta página.
    """
    tickets = Ticket.objects.all()
    form = TicketForm()

    # Procesar formulario de creación de ticket
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect(reverse('tickets:list'))

    context = {
        'tickets': tickets,
        'form': form,
    }
    return render(request, 'tickets/index.html', context)


@login_required
def attend_ticket(request, pk):
    """
    Marca un ticket como atendido.

    Asigna el ticket al usuario que realiza la acción y actualiza el estado a "atendido".
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    # Actualizar estado y usuario asignado
    ticket.status = 'atendido'
    ticket.assigned_to = request.user
    ticket.save()
    return redirect(reverse('tickets:list'))
