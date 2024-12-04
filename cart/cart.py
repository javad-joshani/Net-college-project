from product.models import Product
class Cart:
    def __init__(self,request):
        self.session = request.session 

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self,product,quantity):
        product_id = str(product.uuid)
        product_qty = int(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def product_in_cart(self):
        product_ids = self.cart.keys()
        product = Product.objects.filter(uuid__in=product_ids)
        return product
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def get_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(uuid__in=product_ids)
        product_dict = {str(product.uuid): product for product in products}
        total = 0

        for key, value in self.cart.items():
            key = str(key)
            
            if key in product_dict:
                product = product_dict[key]
                if product.is_special:
                    total += product.get_total_price() * value
                else:
                    total += product.price * value

        return total
    
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty
        self.session.modified = True

        product_return=self.cart
        return product_return
    
    def delete(self ,product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True   