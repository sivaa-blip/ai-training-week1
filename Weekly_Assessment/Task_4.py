"""
Week 1 - Weekly Assessment
Task 4: FastAPI Microservice with Pydantic & REST Endpoints
"""

import json
from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# Pydantic Models for Data Validation
# ---------------------------------------------------------
class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, description="Employee name (cannot be empty)")
    department: str = Field(..., min_length=1, description="Department name (cannot be empty)")
    salary: float = Field(..., gt=0, description="Salary must be strictly greater than 0")


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    pass


# ---------------------------------------------------------
# FastAPI Application Setup
# ---------------------------------------------------------
app = FastAPI(
    title="Employee Data Service",
    description="Yoho HR Employee Data Service API built for Weekly Assessment",
    version="1.0.0"
)

DATA_FILE = Path(__file__).resolve().parent / "employees.json"


def load_employees() -> List[dict]:
    """Reads employee list from employees.json"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        return json.load(file)


def save_employees(employees: List[dict]) -> None:
    """Saves updated employee list back to employees.json"""
    with open(DATA_FILE, mode="w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)


# ---------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------
@app.get("/health", status_code=status.HTTP_200_OK, tags=["System"])
def health_check():
    """Health check endpoint: returns {'status': 'ok'}"""
    return {"status": "ok"}


@app.get("/employees", response_model=List[EmployeeResponse], status_code=status.HTTP_200_OK, tags=["Employees"])
def get_employees():
    """Retrieves all employees from employees.json"""
    return load_employees()


@app.get("/employees/{name}", response_model=EmployeeResponse, status_code=status.HTTP_200_OK, tags=["Employees"])
def get_employee_by_name(name: str):
    """Retrieves a single employee by name; returns 404 if not found"""
    employees = load_employees()
    for emp in employees:
        if str(emp.get("name", "")).lower() == name.lower():
            return emp
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee '{name}' not found")


@app.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED, tags=["Employees"])
def create_employee(emp_data: EmployeeCreate):
    """Creates a new employee with validation (name not empty, salary > 0)"""
    employees = load_employees()
    new_emp = emp_data.model_dump()
    employees.append(new_emp)
    save_employees(employees)
    return new_emp


# ---------------------------------------------------------
# Direct execution helper
# ---------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    print("Starting Employee Data Service on http://127.0.0.1:8000 ...")
    uvicorn.run("Task_4:app", host="127.0.0.1", port=8000, reload=True)
