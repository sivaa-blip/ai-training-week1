from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1)
    department: str = Field(..., min_length=1)
    salary: float = Field(..., gt=0)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    pass
