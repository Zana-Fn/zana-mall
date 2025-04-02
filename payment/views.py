from django.shortcuts import render,redirect, get_object_or_404
from cart.cart import Cart
from django.contrib import messages
from mall.forms import UpdateUserInfoRequired
from .models import Order,OrderItem
from mall.models import Profile
from mall.models import Product
from django.contrib.auth.models import User
# Create your views here.
def payment_success(request):
    return render(request, 'payment/payment_success.html')

def checkout(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    quantities=cart.get_quants()
    total_price=cart.total_p()

    if request.user.is_authenticated:
        shipping_user=Profile.objects.get(user__id=request.user.id)
        shipping_form=UpdateUserInfoRequired(request.POST or None, instance=shipping_user)
        return render(request, 'payment/checkout.html',{'products':cart_products, 'quantities':quantities, 'total_price':total_price,'shipping_form':shipping_form})
    else:
        messages.success(request,'Please first Log In.')
        return redirect('home')

def confirm_order(request):
    if request.method=='POST':
        cart=Cart(request)
        user_profile=Profile.objects.get(user__id=request.user.id)
        cart_products=cart.get_prods()
        quantities=cart.get_quants()
        total_price=cart.total_p()
        user_shipping=request.POST
        request.session['user_shipping']=user_shipping
        
        return render(request, 'payment/confirm.html',{'products':cart_products, 'quantities':quantities, 'total_price':total_price,'shipping_info':user_shipping,'user_profile':user_profile})
    else:
        messages.success(request,'You have not access to this page.')
        return redirect('home')
    
def process_order(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            cart=Cart(request)
            cart_products=cart.get_prods()
            quantities=cart.get_quants()
            total_price=cart.total_p()
            user_shipping=request.session.get('user_shipping')

            phone=user_shipping['phone']
            address1=user_shipping['address1']
            address2=user_shipping['address2']
            city=user_shipping['city']
            user_profile=Profile.objects.filter(user__id=request.user.id)
            
            user_profile.update(phone=phone,address1=address1, address2=address2, city=city)

            full_name=user_profile.first().full_name
            full_address=f"{user_shipping['address1']} \n{user_shipping['address2']}\n{user_shipping['city']}"
            user=request.user
            email=user.email

            new_order=Order(
                user=user,
                full_name=full_name,
                email=email,
                phone=phone,
                shipping_address=full_address,
                amount_paid=total_price,
            )
            new_order.save()

            order=get_object_or_404(Order, id=new_order.pk)

            for product in cart_products:
                prod=get_object_or_404(Product, id=product.id)
                if product.is_sale:
                    price=product.discountedPrice
                else:
                    price=product.price
                
                for k,v in quantities.items():
                    
                    if int(k)== int(product.id):
                        new_item=OrderItem(
                            order=order,
                            product=prod,
                            user=user,
                            quantity=v,
                            price=price
                        )
                        new_item.save()
                        print('item saved')
                    else:
                        pass
            
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]

            user_profile.update(old_cart='')

            messages.success(request,'Ordered successfully.')
            return redirect('home')

    else:
        messages.success(request,'Please first Log In.')
        return redirect('home')