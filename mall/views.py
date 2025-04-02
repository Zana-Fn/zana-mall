from django.shortcuts import render, HttpResponse, redirect
from .models import Product,Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm,UpdateUserForm,UpdatePasswordForm, UpdateUserInfo
from django.db.models import Q
from cart.cart import Cart
import json
from payment.models import Order,OrderItem

def update_info(request):
    if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)
        user_form=UpdateUserInfo(request.POST or None, instance=current_user)
       
        if user_form.is_valid():
            user_form.save()
            
            messages.success(request,'Your user inforrmation has changed')
            return redirect('home')
        
        return render(request, 'update_info.html',{'user_form':user_form})
    else:
        messages.success(request,'You Should first logIn.')
        return redirect('home')

def home(request):
    products=Product.objects.order_by('-discount_p')[:4]
    return render(request, 'index.html', {'products':products})


def shop(request):
    products=Product.objects.all()
    return render(request, 'shop.html', {'products':products})


def about(request):
    return render(request, 'about.html')

def login_user(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            current_user=Profile.objects.get(user__id=request.user.id)
            saved_cart=current_user.old_cart
            if saved_cart:
                converted_cart=json.loads(saved_cart)
                cart=Cart(request)
                for key,value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request,'you loged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'you could not log in !')
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'you Loged out successfully.')
    return redirect('home')


def signup_user(request):

    form=SignUpForm()

    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,'Your account created successfully')
            return redirect('update_info')
        else:
            errors=[str(error) for fieid_errors in form.errors.values() for error in fieid_errors]
            error_message='|'.join(errors)

            messages.error(request,f'There is a problem:  { error_message }')
            return redirect('signup')
    else:
        return render(request, 'signup.html',{'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,'Your inforrmation has changed')
            login(request, current_user)
            return redirect('home')
        
        return render(request, 'update_user.html',{'user_form':user_form})
    else:
        messages.success(request,'You Should first logIn.')
        return redirect('home')
    
def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method =='POST':
            form=UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your Password has changed')
                login(request, current_user)
                return redirect('update')
            else:
                for err in list(form.errors.values()):
                    messages.error(request, err)
                return redirect('update')
        else:
            form=UpdatePasswordForm(current_user)
            return render(request, 'update_password.html',{'form':form})
    else:
        messages.success(request,'You Should first logIn.')
        return redirect('home')
    
    
   
def product(request, pk):
    product=Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def category(request, name):
    try:
        category=Category.objects.get(name=name)
        products=Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    
    except:
        messages.success(request,'There is not this category name.')
        return redirect('shop')
    
def search(request):
    if request.method =='POST':
        searched=request.POST.get('searched')
        searched_products=Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if searched_products:
            return render(request,'search.html',{'products':searched_products})
        else:
            messages.success(request,'There is not this product')
            return render(request,'search.html',{})
    else:

        return render(request,'search.html',{})
    
def orders(request):
    if request.user.is_authenticated:
        delivered_orders=Order.objects.filter(user=request.user, status='Delivered')
        other_orders=Order.objects.filter(user=request.user).exclude(status='Delivered')
        context={
            'delivered':delivered_orders,
            'other':other_orders,
            'delivered_row':0,    
            'other_row':0    
        }
        
        return render(request, 'orders.html', context)
    else:
        messages.success(request,'You have not access to this page. Pleae Log In first')
        return redirect('home')
        
def order_details(request,pk,num):
    if request.user.is_authenticated:
        order=Order.objects.get(id=pk)
        items=OrderItem.objects.filter(order__id=pk)

        return render(request, 'order_details.html', {'order':order, 'items':items,'num':num})
    else:
        messages.success(request,'You have not access to this page. Pleae Log In first')
        return redirect('home')