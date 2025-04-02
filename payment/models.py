from django.db import models
from django.contrib.auth.models import User
from mall.models import Product
from django.db.models.signals import post_save
from django_jalali.db import models as jmodels
import jdatetime

class Order(models.Model):
    STATUS_ORDER=[
        ('Pending','Waiting for Paying'),
        ('Processing','Processing'),
        ('Shipped','Sended to Post'),
        ('Delivered','It has delivered')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=25,null=True, blank=True)
    shipping_address=models.TextField(max_length=150000)
    amount_paid=models.IntegerField(default=0)
    date_ordered=jmodels.jDateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50, choices=STATUS_ORDER, default='Pending')
    last_update=jmodels.jDateTimeField(auto_now=True)

    def get_jalali_date(self):
        return self.last_update.strftime("%Y-%m-%d & %H:%M")

    def __str__(self):
        return f'Order-{str(self.id)}'
    
    def save(self, *args, **kwargs):
        if self.pk:
            old_status=Order.objects.get(id=self.pk).status
            if old_status != self.status:
                self.last_update=jdatetime.datetime.now()

        if self.user:
            self.full_name=f'{self.user.first_name} {self.user.last_name}'.strip()

        super().save(*args, **kwargs)

    
class OrderItem(models.Model):
    order=models.ForeignKey( Order, on_delete=models.CASCADE, null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.IntegerField(default=0)
    def __str__(self):
        if self.user is not None:
            return f'Order Item-{str(self.id)} for {str(self.user)}'
        else:
            return f'Order Item-{str(self.id)}'