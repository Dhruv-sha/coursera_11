from fastapi import APIRouter, HTTPException
from service.models import Product
from service.database import SessionLocal

router = APIRouter()

@router.put("/products/{product_id}")
def update_product(product_id: int, updated_data: dict):
    db = SessionLocal()
    product = db.query(Product).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in updated_data.items():
        setattr(product, key, value)
    
    db.commit()
    db.refresh(product)
    return product
