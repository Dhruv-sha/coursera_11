import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_product_route():
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product_route():
    response = client.put("/products/1", json={"price": 12000})
    assert response.status_code == 200

def test_delete_product_route():
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_all_products_route():
    response = client.get("/products/")
    assert response.status_code == 200

def test_list_by_name_route():
    response = client.get("/products/?name=Phone")
    assert response.status_code == 200

def test_list_by_category_route():
    response = client.get("/products/?category=Electronics")
    assert response.status_code == 200

def test_list_by_availability_route():
    response = client.get("/products/?available=true")
    assert response.status_code == 200
