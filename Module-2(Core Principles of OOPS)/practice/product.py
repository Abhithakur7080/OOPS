class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = None
    def applyDiscount(self, discount):
        self.discount = discount
    def getDiscountedPrice(self):
        return self.price - self.price * self.discount
    def getProductDetails(self):
        return f"Product: {self.name}, Price: {self.price}, Discount: {self.discount}"
    def add_tax(self, tax):
        self.price = self.price + self.price * tax

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    def getDiscountedPrice(self):
        return self.price - self.price * self.discount
    

class ShoppingCart(Product):
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product):
        self.products.remove(product)
    def get_total_price(self):
        return sum(product.price for product in self.products)
    def list_products(self):
        for product in self.products:
            print(product.getProductDetails())

def main():
    product = Product("Laptop", 1000)
    product.applyDiscount(0.1)
    print("Discounted price:", product.getDiscountedPrice())
    discountedProduct = DiscountedProduct("Phone", 500, 0.2)
    print("Discounted price:", discountedProduct.getDiscountedPrice())
    shoppingCart = ShoppingCart()
    shoppingCart.add_product(product)
    shoppingCart.add_product(discountedProduct)
    shoppingCart.list_products()
    print("Total price:", shoppingCart.get_total_price())
if __name__ == "__main__":
    main()