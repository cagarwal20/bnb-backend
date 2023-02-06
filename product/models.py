from django.db import models

# Create your models here.

PRODUCT_CHOICES = (
        ('Whey Protein', 'Whey Protein'),
        ('Creatine', 'Creatine'),
        ('Pre Workout', 'Pre Workout'),
        
    )
SIZE_CHOICES = (
        ('1KG','1KG'),
        ('500GM','500GM'),
        ('250GM','250GM'),
        ('100GM','100GM'),
        
    )
FLAVOUR_CHOICES = (
        ('Chocolate','Chocolate'),
        ('Vanilla','Vanilla'),
        ('Butter scotch','Butter scotch'),
        ('Pista','Pista'),
        
    )
class Product(models.Model):
    product_type = models.CharField(max_length=200,choices=PRODUCT_CHOICES,default=None)
    image_url = models.CharField(max_length=200,default=None)
    size = models.CharField(max_length=20,choices=SIZE_CHOICES,default=None)
    flavour = models.CharField(max_length=20,choices=FLAVOUR_CHOICES,default=None)    
    mrp = models.IntegerField(blank=True)
    discount = models.IntegerField(blank=True)

class Authenticity(models.Model):
    code = models.BigIntegerField(primary_key=True)


class Reviews(models.Model):
    name = models.CharField(max_length=200,blank=False)
    email = models.CharField(max_length=200)
    phone_number  =models.CharField(max_length=200,blank=False)
    feedback = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.name + " " + self.phone_number