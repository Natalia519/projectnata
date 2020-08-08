from django.db import models
from django.template.defaultfilters import register


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField
    unit = models.Model
    photo_url = models.CharField(max_length=1024, default="")
    image = models.ImageField(upload_to='img', default="")

    def __str__(self):
        return self.name


class ProductProp(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductPropsValue(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    productPropsId = models.ForeignKey(ProductProp, on_delete=models.CASCADE)
    value = models.TextField(max_length=1024)

    def __str__(self):
        return self.value


class Goods(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=3)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.productId.name

    class Meta:
        verbose_name_plural = "goods"


@register.filter
def multiply(value, arg, arg2):
    if arg > arg2:
        return value * arg
    return value * arg2