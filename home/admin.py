from django.contrib import admin
from .models import (
    InventarioActivos,
    InventarioPiezas,
    Ticket,
    Producto,
)

admin.site.register(InventarioActivos)
admin.site.register(InventarioPiezas)
admin.site.register(Ticket)
admin.site.register(Producto)
