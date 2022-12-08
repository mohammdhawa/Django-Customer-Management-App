from django.forms import ModelForm
from .models import Customer, Order

class OrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']