from django import forms

from ordersapp.models import Order, OrderItems


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'

class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        exclude = ()

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control py-4'