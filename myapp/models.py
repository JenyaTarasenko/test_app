from django.db import models

class Category(models.Model):
    """
    Модель категории това
    """
    name = models.CharField(max_length=100)



class Product(models.Model):
    """
    Модель това
    """
    name = models.CharField(max_length=100)
    body = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)# чтобы хранить десятичное число фиксированной точности
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)#Это взаимосвязь один-ко-многим: товар принадлежит одной категории, а категория со- держит несколько товаров



