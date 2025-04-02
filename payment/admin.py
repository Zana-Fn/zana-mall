from django.contrib import admin
from .models import Order,OrderItem

admin.site.register(OrderItem)

class OrderItemInLine(admin.TabularInline):
    model=OrderItem
    extra=0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields=['date_ordered','last_update']
    inlines=[OrderItemInLine]
