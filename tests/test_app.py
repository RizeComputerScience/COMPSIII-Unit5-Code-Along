from app import *
import pytest 

def test_clothing_polymorphism():
    '''Test that the __str__ method returns the correct value'''
    clothing_product = ClothingProduct("Pants", 29.99, 54321, "M", "Blue")
    assert str(clothing_product) == "Pants (SKU: 54321) - $29.99 - Size: M, Color: Blue"

def test_electronics_polymorphism():
    '''Test that the __str__ method returns the correct value'''
    electronic_product = ElectronicsProduct("Laptop", 999.99, 67890, 12)
    assert str(electronic_product) == "Laptop (SKU: 67890) - $999.99 - Warranty: 12 months"

def test_cannot_directly_access_sku():
    '''Test that the aku attribute cannot be accessed directly'''
    product1 = Product("Shirt", 19.99, 12345)
    with pytest.raises(AttributeError, match="has no attribute '__sku'"):
        # Attempt to access the sku attribute directly
        _ = product1.__sku

def test_cannot_directly_access_size_and_color():
    '''Test that the size and color attributes cannot be accessed directly'''
    clothing_product = ClothingProduct("Pants", 29.99, 54321, "M", "Blue")
    with pytest.raises(AttributeError, match="has no attribute '__size'"):
        # Attempt to access the size attribute directly
        _ = clothing_product.__size
    with pytest.raises(AttributeError, match="has no attribute '__color'"):
        # Attempt to access the color attribute directly
        _ = clothing_product.__color

def test_get_sku():
    '''Test that the get_sku method returns the correct value'''
    product1 = Product("Shirt", 19.99, 12345)
    assert product1.get_sku() == 12345

def test_set_sku():
    '''Test that the set_sku method sets the correct value'''
    product1 = Product("Shirt", 19.99, 12345)
    product1.set_sku(54321)
    assert product1.get_sku() == 54321

def test_get_size_and_color():
    '''Test that the get_size and get_color methods return the correct values'''
    clothing_product = ClothingProduct("Pants", 29.99, 54321, "M", "Blue")
    assert clothing_product.get_size() == "M"
    assert clothing_product.get_color() == "Blue"

def test_set_size():
    '''Test that the set_size method sets the correct value'''
    clothing_product = ClothingProduct("Pants", 29.99, 54321, "M", "Blue")
    clothing_product.set_size("S")
    assert clothing_product.get_size() == "S"

def test_set_color():
    '''Test that the set_color method sets the correct value'''
    clothing_product = ClothingProduct("Pants", 29.99, 54321, "M", "Blue")
    clothing_product.set_color("Red")
    assert clothing_product.get_color() == "Red"