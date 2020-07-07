from django.db import models
from userprofile.models import User
from goods.models import Goods


class CartState(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Cart(models.Model):
    docStateId = models.ForeignKey(CartState, on_delete=models.PROTECT)
    userId = models.ForeignKey(User, on_delete=models.PROTECT, related_name='userId')
    employeeUserId = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employeeUserId')
    comment = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "<{}: {} - {}>".format(self.pk, self.userId, self.created)


class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.PROTECT)
    goodsId = models.ForeignKey(Goods, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=5, decimal_places=3)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "<{}: {}; {}; {}>".format(self.pk, self.goodsId, self.quantity, self.price)
