import csv
import json
import logging
from pathlib import Path
from typing import List, Optional, Union

import openpyxl
import pymupdf

# Configure logging without printing to stdout
logging.basicConfig(level=logging.ERROR, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "employees.csv"


# 1. Read CSV with DictReader and type hints
def read_employees(path: Path) -> List[dict]:
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# 2. Write JSON
def write_employees_json(employees: List[dict], path: Path) -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)


# 3. Write High Earners CSV (salary > 50000)
def write_high_earners(employees: List[dict], path: Path) -> int:
    high_earners = [e for e in employees if float(e["salary"]) > 50000]
    with open(path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "department", "salary"])
        writer.writeheader()
        for e in high_earners:
            writer.writerow({
                "name": e["name"],
                "department": e["department"],
                "salary": e["salary"],
            })
    return len(high_earners)


# 4. Create and read back Excel workbook
def handle_excel(employees: List[dict], path: Path) -> int:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Employees"
    ws.append(["name", "department", "salary"])
    for e in employees:
        ws.append([e["name"], e["department"], float(e["salary"])])
    wb.save(path)

    # Read back row count excluding header
    wb_read = openpyxl.load_workbook(path)
    sheet = wb_read.active
    count = sheet.max_row - 1
    wb_read.close()
    return count


# 5. Extract text from page 1 of PDF
def extract_pdf_page1(path: Path) -> str:
    if not path.exists():
        # Generate minimal sample PDF if absent
        doc = pymupdf.open()
        page = doc.new_page()
        page.insert_text(
            (50, 50),
            "Yoho Technologies Employee Data Service sample PDF document for Week 1 assignment text extraction testing."
        )
        doc.save(path)
        doc.close()

    doc = pymupdf.open(path)
    text = doc[0].get_text()
    doc.close()
    return text[:100]


# 6. Read file safely with exception logging (no print)
def read_file(path: Path) -> Optional[dict]:
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("File not found: %s", path.name)
    except json.JSONDecodeError:
        logger.error("Invalid JSON format in %s", path.name)
    return None


# 7. Helper functions with type hints
def find_employee(name: str, employees: List[dict]) -> Optional[dict]:
    for emp in employees:
        if emp.get("name", "").lower() == name.lower():
            return emp
    return None


def get_employee_attribute(emp: dict, key: str) -> Union[int, str]:
    val = emp.get(key, "")
    if key == "salary":
        return int(float(val))
    return str(val)


if __name__ == "__main__":
    employees = read_employees(CSV_PATH)

    json_out = BASE_DIR / "employees.json"
    high_earners_out = BASE_DIR / "high_earners.csv"
    excel_out = BASE_DIR / "salary.xlsx"
    pdf_path = BASE_DIR / "sample.pdf"

    write_employees_json(employees, json_out)
    high_earners_count = write_high_earners(employees, high_earners_out)
    excel_rows = handle_excel(employees, excel_out)

    print(f"Rows read: {len(employees)} | High earners written: {high_earners_count}")
    print(f"salary.xlsx created and read back: {excel_rows} rows")

    # Read missing file to trigger logger.error
    read_file(BASE_DIR / "missing.txt")
