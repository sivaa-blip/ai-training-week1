# Python Training

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Repository](https://img.shields.io/badge/Repository-python--training-orange.svg)](https://github.com/sivaa-blip/python-training)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Complete hands-on tasks, daily assignments, datasets, and the weekly assessment for **Python & Data Engineering (Week 1)**.

---

## 📁 Repository Structure

```text
python-training/
├── .gitignore
├── requirements.txt
├── README.md
│
├── Day_1_Sales Report Basics&Functions and Comprehensions/
│   ├── Task_1.py          # Data types, for loop, break/continue, sales report
│   └── Task_2.py          # Functions (*args, **kwargs), list comp, map/filter
│
├── Day_1_Bank Account Class_andInheritance and Overriding/
│   ├── Task_1.py          # Account class, custom InsufficientFundsError, try/except
│   └── Task_2.py          # SavingsAccount inheritance, overriding, min_balance
│
├── Day_3_Data_Cleaning_and_Merging/
│   ├── orders.csv         # Orders dataset
│   ├── customers.csv      # Customers dataset
│   ├── Task_1.py          # Missing values, duplicates, median fillna & groupby
│   └── Task_2.py          # Relational merges: inner, left, outer with indicator
│
├── Day_3_NumPy_and_Pandas_Basics/
│   ├── employees.csv      # 8-row employee dataset
│   ├── Task_1.py          # NumPy array slicing, broadcasting, @ dot product, reshape
│   └── Task_2.py          # head(), info(), describe(), loc, iloc, salary > 50k
│
├── Day_4_Charts_and_Visualizations/
│   ├── employees.csv      # Employee dataset
│   ├── Task_1.py          # Matplotlib visualizations (bar, hist, scatter, line)
│   ├── Task_2.md          # Git & GitHub workflow guide
│   ├── bar_chart.png      # Bar chart output
│   ├── histogram.png      # Histogram output
│   ├── scatter_plot.png   # Scatter plot output
│   ├── line_chart.png     # Line chart output
│   └── all_charts_combined.png # 2x2 subplot figure
│
└── Weekly_Assessment/     # Final 6-Hour Weekly Assessment
    ├── employees.csv      # Employee dataset
    ├── sample.pdf         # Sample PDF for text extraction
    ├── requirements.txt   # Assessment dependencies
    ├── .env.example       # Secrets template
    ├── .gitignore         # Git ignore rules
    ├── Task_1.py          # Core Python & OOP (Bonus, Employee, Manager, Decorator)
    ├── Task_2.py          # File I/O: CSV, JSON, Excel (openpyxl), PDF (pymupdf)
    ├── Task_3.py          # API Client, Session Retry & HMAC-SHA256 Verification
    └── Task_4_FastAPI_Service/ # FastAPI Microservice & Pytest Suite
        ├── pyproject.toml # Black, Ruff & Pytest config
        ├── employees.json # JSON employee storage
        ├── src/
        │   ├── main.py    # FastAPI endpoints (health, get, post)
        │   └── models.py  # Pydantic validation models
        └── tests/
            └── test_main.py # 6 pytest test cases (82% test coverage)
```

---

## 🚀 How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tasks by Folder
```bash
# Day 1 - Sales Report & Functions
cd "Day_1_Sales Report Basics&Functions and Comprehensions"
python Task_1.py
python Task_2.py

# Day 1 - Bank Account & Inheritance
cd "../Day_1_Bank Account Class_andInheritance and Overriding"
python Task_1.py
python Task_2.py

# Day 3 - Data Cleaning & Merging
cd "../Day_3_Data_Cleaning_and_Merging"
python Task_1.py
python Task_2.py

# Day 3 - NumPy & Pandas
cd "../Day_3_NumPy_and_Pandas_Basics"
python Task_1.py
python Task_2.py

# Day 4 - Charts
cd "../Day_4_Charts_and_Visualizations"
python Task_1.py

# Weekly Assessment
cd "../Weekly_Assessment"
python Task_1.py
python Task_2.py
python Task_3.py

# FastAPI Test Suite
cd Task_4_FastAPI_Service
pytest --cov=src
```

---

## 👤 Author

- **Siva** — [GitHub Profile](https://github.com/sivaa-blip)
