from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name = "Category"  # Nombre en singular
        verbose_name_plural = "Categoríes"  # Nombre en plural


