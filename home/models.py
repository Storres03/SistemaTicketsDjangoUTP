from django.db import models

# Create your models here.
class InventarioActivos(models.Model):
    id_activo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    serie = models.CharField(max_length=255)
    encargado = models.IntegerField()  # Podría ser una relación futura con un usuario o técnico

    def __str__(self):
        return self.descripcion
    
class InventarioPiezas(models.Model):
    catalogo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    tecnico_id = models.IntegerField(null=True, blank=True)  # Relación futura con técnico
    cliente_id = models.IntegerField(null=True, blank=True)  # Relación futura con cliente
    descripcion = models.TextField()
    estado_trabajo = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Ticket #{self.id} - {self.estado_trabajo}"
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=255)
    inicio_garantia = models.DateField()
    final_garantia = models.DateField()
    cliente_id = models.IntegerField(null=True, blank=True)  # Relación futura con cliente

    def __str__(self):
        return self.producto
    
