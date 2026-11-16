import csv
from functools import wraps


# 1. Bonus calculation function
def calculate_bonus(salary: float, rate: float = 0.1, *extras, **options) -> float:
    bonus = (salary * rate) + sum(extras)
    if "cap" in options:
        bonus = min(bonus, options["cap"])
    return bonus


# 2. Decorator logging function name before execution
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# 3. Base Employee class
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = float(salary)

    def get_details(self) -> str:
        return f"{self.name} - {int(self.salary)}"

    @property
    def annual_salary(self) -> float:
        return self.salary * 12


# 4. Manager class inheriting Employee
class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    @log_call
    def get_details(self) -> str:
        return f"{self.name} - {int(self.salary)} - Team Size: {self.team_size}"


# 5. Read employees.csv and categorize salaries
with open("employees.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        salary = float(row["salary"])
        name = row["name"]

        if salary < 50000:
            category = "Low Salary"
        elif salary < 70000:
            category = "Medium Salary"
        else:
            category = "High Salary"

        print(f"{name} - {category}")

# 6. Demonstrate Manager and log_call decorator
divya_manager = Manager("Divya", 75000, 5)
print(divya_manager.get_details())
