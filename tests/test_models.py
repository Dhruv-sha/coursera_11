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
