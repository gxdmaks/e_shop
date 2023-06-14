from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)
    added_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)
    desc = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.FloatField()
    product_image = models.ImageField(null=True, blank=True, upload_to='media')
    reviews = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User_Cart(models.Model):
    objects = models.Model
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    added_day = models.DateTimeField(auto_now_add=True)

