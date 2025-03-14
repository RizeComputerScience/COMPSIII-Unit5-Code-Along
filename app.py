# Code from Week 2 and 3 code along
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    
    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    
    def add_items(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def display_cart(self):
        for item in self.items:
            print(f'{item["product"]} - Quantity: {item["quantity"]}')
        print(f"Total: ${self.get_total():.2f}")

# Update clothing_info method to be a _str_ method

class ClothingProduct(Product):
    def __init__(self, name, price, sku, size, color):
        Product.__init__(self, name, price, sku)
        self.size = size
        self.color = color

    def clothing_info(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f} - Size: {self.size}, Color: {self.color}"

# Update electronics_info method to be a _str_ method

class ElectronicsProduct(Product):
    def __init__(self, name, price, sku, warranty_months):
        Product.__init__(self, name, price, sku)
        self.warranty_months = warranty_months
    
    def electronics_info(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f} - Warranty: {self.warranty_months} months"
    
    def under_warranty(self, months):
        if self.warranty_months > months:
            return True
        else:
            return False