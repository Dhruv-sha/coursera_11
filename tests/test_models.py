import pytest
from myapp.models import Product

@pytest.mark.django_db
def test_read_product():
    # Arrange
    product = Product.objects.create(name="Laptop", price=50000)

    # Act
    fetched = Product.objects.get(id=product.id)

    # Assert
    assert fetched.name == "Laptop"
    assert fetched.price == 50000


@pytest.mark.django_db
def test_update_product():
    # Arrange — create a product
    product = Product.objects.create(name="Phone", price=10000)

    # Act — update product details
    product.price = 12000
    product.save()

    # Fetch updated record
    updated_product = Product.objects.get(id=product.id)

    # Assert — check if update worked
    assert updated_product.price == 12000


@pytest.mark.django_db
def test_delete_product():
    product = Product.objects.create(name="Laptop", price=50000)
    product_id = product.id
    product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product_id)

@pytest.mark.django_db
def test_list_all_products():
    Product.objects.create(name="Phone", price=10000)
    Product.objects.create(name="Tablet", price=20000)
    all_products = Product.objects.all()
    assert len(all_products) == 2

@pytest.mark.django_db
def test_find_by_name():
    product = Product.objects.create(name="Camera", price=15000)
    found = Product.objects.filter(name="Camera").first()
    assert found.id == product.id

@pytest.mark.django_db
def test_find_by_category():
    Product.objects.create(name="Laptop", category="Electronics")
    Product.objects.create(name="Shirt", category="Clothing")
    electronics = Product.objects.filter(category="Electronics")
    assert electronics.count() == 1

@pytest.mark.django_db
def test_find_by_availability():
    Product.objects.create(name="Mouse", stock=0)
    Product.objects.create(name="Keyboard", stock=5)
    available = Product.objects.filter(stock__gt=0)
    assert available.count() == 1
