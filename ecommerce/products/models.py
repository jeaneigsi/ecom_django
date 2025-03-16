from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    description= models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description= models.TextField()
    price= models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='products/images',blank=True,null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
