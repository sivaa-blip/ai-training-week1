import json
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from src.main import app, DATA_FILE

client = TestClient(app)

SAMPLE_DATA = [
    {"name": "Arun", "department": "Sales", "salary": 30000.0},
    {"name": "Priya", "department": "HR", "salary": 45000.0},
    {"name": "Rahul", "department": "IT", "salary": 60000.0},
]


@pytest.fixture(autouse=True)
def setup_test_file():
    original_content = None
    if DATA_FILE.exists():
        original_content = DATA_FILE.read_text(encoding="utf-8")

    with open(DATA_FILE, mode="w", encoding="utf-8") as file:
        json.dump(SAMPLE_DATA, file)

    yield

    if original_content is not None:
        DATA_FILE.write_text(original_content, encoding="utf-8")


# 1. Health check test
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# 2. List all employees test
def test_get_employees_list():
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) >= 3


# 3. Successful retrieval by name
def test_get_employee_success():
    response = client.get("/employees/Arun")
    assert response.status_code == 200
    assert response.json()["name"] == "Arun"


# 4. Employee not found (404)
def test_get_employee_not_found():
    response = client.get("/employees/Ravi")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


# 5. Invalid salary <= 0 (422)
def test_create_employee_invalid_salary():
    payload = {"name": "TestUser", "department": "QA", "salary": -5}
    response = client.post("/employees", json=payload)
    assert response.status_code == 422


# 6. Empty name validation (422)
def test_create_employee_empty_name():
    payload = {"name": "", "department": "QA", "salary": 50000}
    response = client.post("/employees", json=payload)
    assert response.status_code == 422
