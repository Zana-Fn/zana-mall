from mall.models import Product,Profile

class Cart:
    def __init__(self, request):
        self.session=request.session
        self.request=request
        cart=self.session.get('session_key')
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}
        self.cart=cart

    def db_add(self, product, quantity):
        product_id=str(product)
        product_qty=int(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=product_qty
        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            db_cart=str(self.cart).replace('\'','\"')
            current_user.update(old_cart=str(db_cart))

    def add(self, product, quantity):
        product_id=str(product.id)
        product_qty=int(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)
        self.session.modified=True

        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            db_cart=str(self.cart).replace('\'','\"')
            current_user.update(old_cart=str(db_cart))



    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        products_id=self.cart.keys()
        products=Product.objects.filter(id__in=products_id)
        return products
    
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    def update(self, product_id, quantity):
        product_id=str(product_id)
        product_qty=int(quantity)

        ourcart=self.cart
        ourcart[product_id]=product_qty
        self.session.modified=True
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            db_cart=str(self.cart).replace('\'','\"')
            current_user.update(old_cart=str(db_cart))

        return self.cart

    def delete(self, product_id):
        product_id=str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified=True
        if self.request.user.is_authenticated:
            current_user=Profile.objects.filter(user__id=self.request.user.id)
            db_cart=str(self.cart).replace('\'','\"')
            current_user.update(old_cart=str(db_cart))
        return self.cart
    
    def total_p(self):
        total_price=0
        for key,value in self.cart.items():
            product=Product.objects.get(id=int(key))
            quantity=value
            if product.is_sale:
                product_price=product.discountedPrice
                total_price+=product_price*quantity
            else:
                product_price=product.price
                total_price+=product_price*quantity

        return total_price