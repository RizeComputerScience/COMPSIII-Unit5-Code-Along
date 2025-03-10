from app import Product, ShoppingCart, ClothingProduct, ElectronicsProduct

def main():
    # Code from last week's code along
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    pants = ClothingProduct("Jeans", 19.99, "901234", "32x32", "Blue")
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    tv = ElectronicsProduct("Samsung TV", 999.99, "345678", 24)

    cart = ShoppingCart()
    cart.add_items(laptop)
    cart.add_items(headphones, 2)
    cart.add_items(shirt)
    cart.add_items(pants)
    cart.add_items(phone)
    cart.add_items(tv)

    print('\nCart Info:')
    cart.display_cart()
    print(cart)
    # End code from last week's code along





main()