from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:

        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.1)])
    image = CloudinaryField('image', null=True, blank=True)
