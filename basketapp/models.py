from django.db import models
from authapp.models import User

from mainapp.models import Product


class Basket(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user.username}, товар {self.product.name}'

    def total_sum(self):
        return self.quantity * self.product.price
