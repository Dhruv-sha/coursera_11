import factory
from myapp.models import Product  # adjust this to your actual model path

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    price = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    stock = factory.Faker("random_int", min=0, max=100)
