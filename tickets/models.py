from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """
    Modelo sencillo para la gestión de tickets.

    Cada ticket tiene un título, descripción, usuario creador,
    usuario asignado (quien atiende el ticket), estado y fechas de creación y actualización.
    """

    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('atendido', 'Atendido'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets_created',
        help_text='Usuario que crea el ticket'
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tickets_assigned',
        help_text='Usuario que atiende el ticket'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f"Ticket #{self.id} - {self.title}"
