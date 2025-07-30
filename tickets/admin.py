from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Configuración de Django admin para el modelo Ticket.
    """

    list_display = ('id', 'title', 'status', 'created_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'created_by__username', 'assigned_to__username')
