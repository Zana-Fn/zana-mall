from django.shortcuts import render, get_object_or_404
from .cart import Cart
from mall.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    quantities=cart.get_quants()
    total_price=cart.total_p()
    return render(request, 'cart_summary.html',{'cart_products':cart_products, 'quantities':quantities, 'total_price':total_price})

def cart_add(request):
    cart=Cart(request)

    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product=get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity=cart.__len__()
        response=JsonResponse({'qty':cart_quantity})
        messages.success(request,'The Product added to Cart')
        return response

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        cart.delete(product_id)
        
        response=JsonResponse({'qty':product_id})
        messages.success(request,'The Product Deleted from Cart')
        return response

def cart_update(request):
    cart=Cart(request)

    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        cart.update(product_id=product_id, quantity=product_qty)
        messages.success(request,'The Number of Product Edited successfully.')
        response=JsonResponse({'qty':product_qty})
        return response
    
