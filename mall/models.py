from django.db import models
from django.db.models.signals import post_save
import re, math
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import jdatetime

class Category(models.Model):
    name=models.CharField(max_length=55)
    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=25, blank=True)
    date_modified=models.DateTimeField(User, auto_now=True)
    phone=models.CharField(max_length=25, blank=True)
    address1=models.CharField(max_length=250, blank=True)
    address2=models.CharField(max_length=250, blank=True)
    city=models.CharField(max_length=25, blank=True)
    old_cart=models.CharField(max_length=300,blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}'
    
    def save(self, *args, **kwargs):
        if self.user:
            self.full_name=f'{self.user.first_name} {self.user.last_name}'.strip()

        super().save(*args, **kwargs)


    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)



class Product(models.Model):
    SIZES=(
        ('M',32),
        ('L',42),
        ('XL',52),
    )
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=500,blank=True, default='Lorem ipsum odor amet, consectetuer adipiscing elit. Risus malesuada erat venenatis sed suspendisse dictum. Ullamcorper placerat aliquam sit rhoncus; class blandit varius. Primis diam aptent mus maecenas inceptos quam.', null=True)
    price=models.IntegerField(default=0)
    size=models.CharField(max_length=4, default=42, choices=SIZES, null=True, blank=True)
    main_image=models.ImageField(upload_to='upload/product/main/', null=True, blank=True)
    extra_image=models.ImageField(upload_to='upload/product/extra/', null=True, blank=True)
    star=models.IntegerField(default=4, validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_sale=models.BooleanField(default=False)
    discount_p=models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if self.category.name not in ['clothes','jeans']:
            self.size=None
        super().save(*args, **kwargs)


    @property
    def discountedPrice(self):
        return math.trunc((1-(int(self.discount_p)/100))*self.price)
    
    def __str__(self):
        return f'{self.name}'
    
