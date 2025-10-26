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


    import pytest
from myapp.models import Product

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

