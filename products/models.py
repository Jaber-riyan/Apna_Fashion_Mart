from django.db import models
from categories.models import CategoryModel
from django.contrib.auth.models import User

# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='products/image/product_image',null=True,blank=True)
    shipping_cost = models.IntegerField(null=True,blank=True,default=50)
    
    
    def __str__(self):
        return f'{self.product_name} - {self.category.category_name}'
    
    
class Chart(models.Model):
    product = models.ForeignKey(ProductModel,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    
    
    def __str__(self):
        return f'{self.user.first_name} - {self.product.product_name}'