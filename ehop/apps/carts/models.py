from django.db import models
from django.contrib.auth.models import User
from ..products.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_price(self):
        return sum([self.cart_item.product_price*self.cart_item.quantity for self.cart_item in self.cart_item.all()])

    price = models.DecimalField(decimal_places=2, default=total_price)

    def ready_to_pay(self):
        if self.cart_item.status:
            return True

    cart_status = property(ready_to_pay)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart', related_name='cart_item')
    quantity = models.IntegerField(default=1)
    product_price = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def cart_item_status(self):
        if self.product.available and self.product.amount >= self.quantity:
            return True
        elif self.product.available and self.product.amount < self.quantity:
            return False
        else:
            return False

    status = property(cart_item_status)


