from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """Formulario para crear/editar productos con CSRF automático"""
    class Meta:
        model = Producto
        # ✅ Se agregan imagen_archivo e imagen_url
        fields = ['nombre', 'categoria', 'precio', 'stock', 'sku', 'imagen_archivo', 'imagen_url']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU único'}),
            'imagen_archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://ejemplo.com/imagen.jpg'
            }),
        }