from django.contrib import admin
from .models import Category, Product, Profile
from django.contrib.auth.models import User  

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)

class ProfileInLine(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):
    model=User
    fields=['username','first_name','email']
    inlines=[ProfileInLine]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)