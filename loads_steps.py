from behave import given
from service.models import Product
from service.database import SessionLocal

@given('the following products exist')
def step_impl(context):
    db = SessionLocal()
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            price=float(row['price']),
            stock=int(row['stock'])
        )
        db.add(product)
    db.commit()
