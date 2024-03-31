import pytest
from category_and_product import Category, Product

def test_category_initialization():
    product1 = Product("Laptop", "High-performance laptop", 1500.00, 10)
    product2 = Product("Mouse", "Wireless mouse", 30.00, 20)
    products = [product1, product2]
    category = Category("Electronics", "Electronic devices", products)


    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert category.product == products

def test_product_initialization():
    product = Product("Keyboard", "Mechanical keyboard", 100.00, 15)

    assert product.name == "Keyboard"
    assert product.description == "Mechanical keyboard"
    assert product.price == 100.00
    assert product.count_in_stock == 15

def test_count_products_and_categories():
    initial_categories = Category.total_categories
    initial_products = Category.total_unique_products
    product1 = Product("Headphones", "Noise-cancelling headphones", 200.00, 5)
    product2 = Product("Smartphone", "Latest smarthphone model", 800.00, 8)
    products = [product1, product2]
    category = Category("Gadgets", "Electronic gadgets", products)

    assert Category.total_categories == initial_categories + 1
    assert Category.total_unique_products == initial_products + len(products)

