import pytest
from app_2 import app  # import your Flask app


@pytest.fixture
def client():
    # Flask has a test client we can use
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome to the Food Api" in res.data


def test_get_foods(client):
    res = client.get("/foods")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)  # should return a list of foods


def test_add_food(client):
    res = client.post("/foods", json={"name": "Mango", "calories": 150})
    assert res.status_code == 201
    data = res.get_json()
    assert data["name"] == "Mango"
    assert data["calories"] == 150


def test_update_food(client):
    res = client.put("/foods/1", json={"calories": 120})
    assert res.status_code == 200
    data = res.get_json()
    assert data["calories"] == 120


def test_delete_food(client):
    res = client.delete("/foods/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["message"] == "Food deleted"
