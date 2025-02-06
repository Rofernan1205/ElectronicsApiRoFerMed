from django.db import models
from categories.models import Category
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    trade_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Trade name")
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    model = models.CharField(max_length=80, verbose_name='Model')
    brands = models.CharField(max_length=100, verbose_name="Brands")
    processor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Processor")
    screen_size = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name="Screen size")
    height = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name="Height")
    width = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True, verbose_name="Width")
    country_origin = models.CharField(max_length=60, verbose_name="Country of origin")
    accessories = models.CharField(max_length=400, verbose_name="Accessories")
    image = CloudinaryField('image')
    img = CloudinaryField('img')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Product"  # Nombre en singular
        verbose_name_plural = "Products"  # Nombre en plural
