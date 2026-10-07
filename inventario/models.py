from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    """Modelo de Categoría de productos"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo de Producto con FK a Categoría"""
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
        verbose_name='Categoría'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True)
    
    # ✅ NUEVOS CAMPOS DE IMAGEN
    imagen_archivo = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True,
        verbose_name='Imagen (archivo)'
    )
    imagen_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Imagen (URL)',
        help_text='Pega una URL de imagen (ej: https://ejemplo.com/imagen.jpg)'
    )
    
    fecha_ingreso = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_ingreso', 'nombre']

    def __str__(self):
        return f"{self.nombre} (SKU: {self.sku})"

    def get_absolute_url(self):
        return reverse('admin_panel')

    # ✅ MÉTODO PARA OBTENER LA IMAGEN (Prioriza archivo, luego URL)
    def get_imagen(self):
        if self.imagen_archivo:
            return self.imagen_archivo.url
        elif self.imagen_url:
            return self.imagen_url
        return None