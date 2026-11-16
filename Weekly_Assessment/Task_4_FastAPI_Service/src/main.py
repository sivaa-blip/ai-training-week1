import json
from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException, status
from src.models import EmployeeCreate, EmployeeResponse

app = FastAPI(title="Employee Data Service")

DATA_FILE = Path(__file__).resolve().parent.parent / "employees.json"


def load_employees() -> List[dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        return json.load(file)


def save_employees(employees: List[dict]) -> None:
    with open(DATA_FILE, mode="w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok"}


@app.get("/employees", response_model=List[EmployeeResponse], status_code=status.HTTP_200_OK)
def get_employees():
    return load_employees()


@app.get("/employees/{name}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK)
def get_employee_by_name(name: str):
    employees = load_employees()
    for emp in employees:
        if emp.get("name", "").lower() == name.lower():
            return emp
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")


@app.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(emp_data: EmployeeCreate):
    employees = load_employees()
    new_emp = emp_data.model_dump()
    employees.append(new_emp)
    save_employees(employees)
    return new_emp
