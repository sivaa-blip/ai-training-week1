# Python & Data Engineering — Complete Beginner to Pro Learning Guide
# பைதான் முழுமையான ஆரம்ப வழிகாட்டி (English & Tanglish)

This guide explains every single task and concept you have completed in Week 1, from absolute zero, step-by-step.
Each topic has **English on top** and **Tanglish below** with code examples and line-by-line reasoning.

---

## 📑 Table of Contents (பொருளடக்கம்)
1. [Day 1: Python Basics, Data Types & Control Flow](#day-1-python-basics-data-types--control-flow)
2. [Day 1: Functions, *args, **kwargs & Comprehensions](#day-1-functions-args-kwargs--comprehensions)
3. [Day 1: Object-Oriented Programming (OOP) & Custom Exceptions](#day-1-object-oriented-programming-oop--custom-exceptions)
4. [Day 3: Data Cleaning, Missing Values & GroupBy (Pandas)](#day-3-data-cleaning-missing-values--groupby-pandas)
5. [Day 3: Table Merges (Inner, Left, Outer Joins)](#day-3-table-merges-inner-left-outer-joins)
6. [Day 3: NumPy Multi-Dimensional Arrays & Matrix Math](#day-3-numpy-multi-dimensional-arrays--matrix-math)
7. [Day 4: Data Visualization with Matplotlib](#day-4-data-visualization-with-matplotlib)
8. [Weekly Assessment: Advanced File I/O (CSV, JSON, Excel, PDF)](#weekly-assessment-advanced-file-io-csv-json-excel-pdf)
9. [Weekly Assessment: Resilient API Client & HMAC Webhook Security](#weekly-assessment-resilient-api-client--hmac-webhook-security)
10. [Weekly Assessment: FastAPI Microservice & Pytest](#weekly-assessment-fastapi-microservice--pytest)

---

## 1. Day 1: Python Basics, Data Types & Control Flow

### English:
Python has 7 fundamental data types:
- `int`: Whole numbers like `42`
- `float`: Decimal numbers like `3.14`
- `str`: Text wrapped in quotes like `"Hello"`
- `list`: Ordered, mutable collection in brackets `[1, 2, 3]`
- `dict`: Key-value pairs in braces `{"name": "Arun", "salary": 30000}`
- `set`: Unique unordered values `{1, 2, 3}` (duplicates are automatically dropped)
- `tuple`: Immutable (unchangeable) collection in parentheses `(10, 20)`

**Loops and Flow Controls:**
- `for item in list:` loops through each element one by one.
- `continue`: Skips the rest of the current iteration and jumps to the next item (e.g., skip `0` or negative values).
- `break`: Stops the loop completely immediately (e.g., stop when sales target exceeds 30,000).

### Tanglish:
Python-la data-va store panna 7 mukkiyamana types irukku:
- `int`: Muzhumayana enngal (whole numbers), e.g. `42`
- `float`: Decimal dot vecha numbers, e.g. `3.14`
- `str`: Text / vaarthai, e.g. `"Hello"`
- `list`: Square bracket `[ ]` kula pala data-va store panna mudiyum, change-um pannalam.
- `dict`: Key-Value pair, dictionary maari: `{"name": "Arun"}` (Name thaan key, Arun thaan value).
- `set`: Unique values mattum thaan irukkum. Duplicates irundha auto-va delete aagidum `{1, 2}`.
- `tuple`: Parentheses `( )` kula irukkum. Oru vaati create pannita change panna mudiyaadhu (immutable).

**Loop Controls:**
- `for loop`: Oru list-la irukura ovvoru value-aiyum line-by-line check panna use aagudhu.
- `continue`: Indha value theva illa, adutha value-ku poidu nu solradhukku `continue` use panrom (e.g., sales `0` illa negative-ah irundha skip panrom).
- `break`: Target reach aana udane loop-ai vittu veliya vaa nu solradhukku `break` use panrom.

```python
sales = [12000, 0, 8500, 15000, -200, 9800]
total = 0

for sale in sales:
    if sale <= 0:
        print(f"Skipped invalid value {sale}")
        continue  # Skip zero/negative values

    total += sale
    print(f"Added {sale} total {total}")

    if total > 30000:
        break  # Target achieved, exit loop!

if total > 30000:
    print(f"Target reached. Stopped at {total}")
```

---

## 2. Day 1: Functions, *args, **kwargs & Comprehensions

### English:
- **Default arguments**: `def apply_discount(price, discount=10)` — if you don't pass a discount, it automatically defaults to `10%`.
- `*args` (Positional arguments): Accepts any number of numeric values as a tuple, so `total(5, 10, 15)` sums all of them.
- `**kwargs` (Keyword arguments): Accepts any number of named arguments as a dictionary (e.g., `describe(name="Arun", role="Dev")`).
- **List Comprehension**: A compact 1-line syntax to filter or transform lists: `[p for p in prices if p > 1000]`.
- **`map(lambda, list)`**: Transforms every single element in a list (e.g., calculates price with 18% GST).
- **`filter(lambda, list)`**: Keeps only elements that evaluate to `True` (e.g., prices below 1000).

### Tanglish:
- **Default Arguments**: Function-la value tharalana automatic-ah edhuthuka vendiya default value (e.g. `discount=10`).
- `*args`: Function-ku evalo numbers venaalum anuppalam, athu ellathayum oru list/tuple maari eduthu kootikkum (`sum`).
- `**kwargs`: Key=Value maari evalo per-ah venaalum function-ku anuppalam (`describe(name="Arun")`).
- **List Comprehension**: 4 line for loop-ah ore line-la ezhudhi list create panra easy method: `[p for p in prices if p > 1000]`.
- **`map()`**: List-la irukra ovvoru item-kum oru calculation panna `map()` use aagum (e.g., 18% GST calculate panna: `price * 1.18`).
- **`filter()`**: List-la irundhu namakku thevayana items mattum filter panni edukka (e.g. 1000-ku keezha irukra prices).

```python
# Function with default value
def apply_discount(price, discount=10):
    return float(price - (price * discount / 100))

# Flexible arguments
def total(*args):
    return sum(args)

prices = [500, 1200, 800, 2500, 300]

# List comprehension: Filter prices above 1000
above_1000 = [p for p in prices if p > 1000]

# map(): Add 18% GST
with_gst = list(map(lambda p: round(p * 1.18, 2), prices))

# filter(): Keep prices below 1000
below_1000 = list(filter(lambda p: p < 1000, prices))
```

---

## 3. Day 1: Object-Oriented Programming (OOP) & Custom Exceptions

### English:
- **Class**: A blueprint (e.g., `Account` blueprint defines what a bank account has: owner, balance, and what it can do: deposit, withdraw).
- **Object / Instance**: A real-world instance created from the blueprint (e.g., `account = Account("Arun", 1000)`).
- **`self`**: Refers to the specific object currently being operated on.
- **Inheritance (`class SavingsAccount(Account)`)**: Reuses everything from the parent `Account` class and adds specialized logic (like minimum balance protection).
- **`super().__init__()`**: Calls the parent constructor so we don't repeat code.
- **Custom Exceptions**: Creating our own error class (`class InsufficientFundsError(Exception): pass`) so we can raise custom, clear domain errors when a user tries to withdraw more money than they have.
- **`try / except / finally`**:
  - `try`: Code that might trigger an error.
  - `except`: Catches and handles the error gracefully without crashing.
  - `finally`: Guaranteed to run no matter what happens (e.g., closing transactions or files).

### Tanglish:
- **Class-na enna?**: Oru blueprint (maadhiri vadivam). Bank Account epdi irukkanum nu oru template design panrom.
- **Object-na enna?**: Andha blueprint-ah vechu create panna unmaiyana account (e.g. Arun-oda account).
- **`self`-na enna?**: Ennodaya account, ennodaya balance nu andha specific aaloda details-ah point panna `self` use panrom.
- **Inheritance (Thatha -> Appa -> Pulla)**: `Account` class-la irukra ella features-aiyum `SavingsAccount` appadiye eduthukkum (`super()`). Extra-va `min_balance=500` constraint mattum add panrom.
- **Custom Exception**: Account-la balance illadha appo Python standard error tharaama, namma sonna `InsufficientFundsError` nu azhaga error kaatta use aagum.
- **`try/except/finally`**:
  - `try`: Error vara chance irukura code.
  - `except`: Error vandha program crash aagama handle panna.
  - `finally`: Error vandhalum varalanalum kandippa run aaga vendiya code (e.g., `Transaction finished`).

```python
class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds: balance {self.balance}, requested {amount}")
        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")

# Child class inheriting Account
class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0, min_balance: float = 500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        # Cannot let balance drop below min_balance
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError(f"Insufficient funds: balance {self.balance}, requested {amount}")
        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")
```

---

## 4. Day 3: Data Cleaning, Missing Values & GroupBy (Pandas)

### English:
When real-world CSV files arrive, they often have **dirty data**: duplicate rows, missing amounts, or wrong column types (numbers stored as text).
- `pd.read_csv("orders.csv")`: Loads the file into a tabular DataFrame.
- `df.isna().sum()`: Counts how many missing (null/empty) values exist in each column.
- `df.duplicated().sum()`: Counts duplicate rows.
- `df.drop_duplicates()`: Drops duplicate rows to prevent double-counting revenue.
- `pd.to_numeric(df["amount"])`: Converts text numbers into true mathematical floats.
- `df["amount"].fillna(median_value)`: Fills empty rows with the middle value (median), which is resistant to extreme outliers.
- `df.groupby("customer_id").agg(...)`: Groups all orders by customer and calculates both the total spent and order count.

### Tanglish:
Real-world data epovume clean-ah irukaadhu. Sila idathula empty-ah irukkum, sila rows repeat aagum (duplicates).
- `pd.read_csv()`: Excel sheet maari CSV file-ah Python memory-la load pannum.
- `df.isna().sum()`: Endha endha column-la data missing nu count pannum.
- `df.duplicated().sum()`: Orey row rendu vaati repeat aagudha nu check pannum.
- `df.drop_duplicates()`: Repeat aana rows-ah delete panni clean pannum.
- `fillna(median)`: Amount column-la missing data irundha, athoda nadu value (median)-ah vechu fill pannidum.
- `df.groupby("customer_id").agg(...)`: Oru customer 3 vaati order pannirundha, avaru motham evalo vaati order pannaru, motham evalo rooba selavu pannaru nu summary edukkum.

```python
import pandas as pd

df = pd.read_csv("orders.csv")

# 1. Detect duplicates and nulls
missing = df["amount"].isna().sum()
duplicates = df.duplicated().sum()

# 2. Clean data
df = df.drop_duplicates()
df["amount"] = pd.to_numeric(df["amount"])
median_val = df["amount"].median()
df["amount"] = df["amount"].fillna(median_val)
df["order_id"] = df["order_id"].astype(str)

# 3. Aggregate totals per customer
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)
```

---

## 5. Day 3: Table Merges (Inner, Left, Outer Joins)

### English:
Relational data is stored in separate tables (`orders.csv` has orders; `customers.csv` has names). To combine them:
1. **Inner Join (`how='inner'`)**: Keeps only records where `customer_id` exists in **BOTH** tables. (If customer 104 has an order but isn't registered in the customers table, they get dropped).
2. **Left Join (`how='left'`)**: Keeps **ALL** records from the left table (customers), matching orders where available. If a customer has no orders, their `order_id` shows as `NaN` (useful to find inactive users like Divya).
3. **Full Outer Join (`how='outer', indicator=True`)**: Keeps **EVERYTHING** from both tables. The `_merge` column tells you whether a row came from both (`both`), left only, or right only (useful to detect unregistered orders).

### Tanglish:
Rendu table-ah onna serkka `pd.merge()` use panrom:
1. **Inner Join**: Rendu table-layum common-ah irukra data mattum thaan varum. Oru customer order pannirundha mattum thaan varuvaru.
2. **Left Join**: Left table-la irukra ella customers-um varuvanga. Avaru oru order kooda pannala naalum avar name varum (e.g. Yaarulaam order-eh pannala nu kandupidikka idhu use aagum).
3. **Outer Join**: Rendu table-la irukra motha data-vum varum. Yaaravadhu customer registration pannama order pottangala nu check panna idhu use aagum.

```python
# 1. Inner Join
inner_df = pd.merge(orders, customers, on="customer_id", how="inner")

# 2. Left Join (Find customers who never placed an order)
left_df = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = left_df[left_df["order_id"].isna()]["name"].tolist()

# 3. Outer Join (Find ghost orders without registered customer)
outer_df = pd.merge(orders, customers, on="customer_id", how="outer", indicator=True)
no_customer = outer_df[outer_df["_merge"] == "left_only"]["customer_id"].tolist()
```

---

## 6. Day 3: NumPy Multi-Dimensional Arrays & Matrix Math

### English:
- **Why NumPy?**: Regular Python lists are slow and cannot do vector math directly. NumPy arrays are written in C, ultra-fast, and handle multi-dimensional tables effortlessly.
- `marks.shape`: `(4, 3)` means 4 rows (students) and 3 columns (subjects).
- **Averages along axes**:
  - `axis=1`: Computes horizontal row averages (average score of each student across subjects).
  - `axis=0`: Computes vertical column averages (average score of each subject across all students).
- **Broadcasting (`marks + 5`)**: Automatically adds `5` to every single cell without needing a double `for` loop!
- **Matrix Multiplication (`@`)**: Multiplies subject scores by category weights `[0.3, 0.3, 0.4]` to compute the final weighted average.

### Tanglish:
- **Yen NumPy use panrom?**: Normal Python list romba slow. Aana NumPy array C language-la ezhudhirukadhu nala rathathula jet vecha maari fast-ah irukkum.
- `marks.shape`: `(4, 3)` na 4 students, 3 subjects nu artham.
- **`axis=1` vs `axis=0`**:
  - `axis=1`: Row-wise average (ovvoru student-oda average mark).
  - `axis=0`: Column-wise average (ovvoru subject-oda average mark).
- **Broadcasting (`marks + 5`)**: For loop poda theva illa, direct-ah `+ 5` pota array kula irukra ella marks-layum 5 grace marks add aagidum!
- **Matrix Multiplication (`@`)**: Weightage mark calculate panna use aagum (e.g., 30% first sub, 30% second sub, 40% third sub).

```python
import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

# Slicing: First two students, last subject
print(marks[:2, -1])

# Row average (student) & column average (subject)
student_averages = marks.mean(axis=1)
subject_averages = marks.mean(axis=0)

# Broadcasting (add 5 grace marks to all)
grace_marks = marks + 5

# Weighted dot product
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = marks @ weights
```

---

## 7. Day 4: Data Visualization with Matplotlib

### English:
Visual charts make complex numbers understandable at a single glance:
- **Bar Chart (`plt.bar`)**: Best for comparing categories (e.g., average salary per department). `plt.bar_label()` puts the exact numbers right on top of each bar.
- **Histogram (`plt.hist`)**: Shows the distribution/frequency of continuous numbers by grouping them into bins (e.g., how many employees earn between 30k-45k vs 45k-60k).
- **Scatter Plot (`plt.scatter`)**: Plots individual points on an X-Y plane with color coding to spot correlations or outliers.
- **Line Chart (`plt.plot`)**: Best for tracking trends over time (e.g., monthly sales from Jan to Jun).
- **`plt.savefig("chart.png")`**: Exports the rendered chart to a PNG file so it can be emailed, embedded in reports, or pushed to GitHub.

### Tanglish:
Numbers-ah visual-ah chart maari paaka Matplotlib use panrom:
- **Bar Chart**: Oru oru department-kum average salary evalo nu bar chart pottu compare panna.
- **Histogram**: Salary distribution-ah frequency bins pottu paaka (evalo per kammi salary, evalo per athigam).
- **Scatter Plot**: Ovvoru employee-yum pulli vechu (dots) color panni paaka.
- **Line Chart**: Kaalathula maari varra trends paaka (e.g., Jan to Jun sales increase aagudha illaya).
- **`plt.savefig()`**: Chart-ah PNG image file-ah computer-la save panna.

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("employees.csv")

# 1. Bar Chart
avg_salary = df.groupby("department")["salary"].mean()
bars = plt.bar(avg_salary.index, avg_salary.values, color="skyblue")
plt.bar_label(bars, fmt="%.0f")
plt.title("Average Salary per Department")
plt.savefig("bar_chart.png")
plt.close()

# 2. Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]
plt.plot(months, sales, marker="o", color="green")
plt.title("Monthly Sales")
plt.savefig("line_chart.png")
plt.close()
```

---

## 8. Weekly Assessment: Advanced File I/O (CSV, JSON, Excel, PDF)

### English:
In production data engineering, data never stays in one format. You must be able to convert and extract between multiple file types:
- `pathlib.Path`: Object-oriented file path handling that works consistently across Windows (`\`) and Linux/Mac (`/`).
- `json.dump(data, file, indent=4)`: Serializes Python dictionaries into clean, indented JSON files.
- `openpyxl.Workbook()`: Programmatically creates formatted Excel `.xlsx` spreadsheets with sheets and headers.
- `pymupdf.open(path)`: Fast C-based PDF engine to extract raw text from page 1 of any document.
- `logging.getLogger(__name__)`: Enterprise standard for recording error events into logs without polluting terminal stdout with `print()`.

### Tanglish:
Real-world company-la data oru format-la mattum irukkaadhu. CSV, JSON, Excel, PDF nu maathi maathi convert panna vendiyirukkum:
- `pathlib.Path`: Windows-layum Linux-layum path issue varaama path handle panna modern vazhi.
- `json.dump()`: Python list/dict-ah JSON file-ah save panna.
- `openpyxl`: Excel `.xlsx` file-ah Python moolama create panni data ezhudha.
- `pymupdf`: PDF file kula irukra text-ah read panni veliya edukka.
- `logging`: Program-la error vandha `print()` podama, background log-la record panni vekka.

---

## 9. Weekly Assessment: Resilient API Client & HMAC Webhook Security

### English:
- **`python-dotenv`**: Loads secret API keys from a `.env` file into `os.getenv()` so credentials are never hardcoded or committed to GitHub.
- **`urllib3.util.Retry`**: If a third-party server temporarily glitches with HTTP `500, 502, 503, 504`, the client automatically retries up to 3 times with exponential backoff (`backoff_factor=1`) instead of failing immediately.
- **Safe Dictionary Traversal (`.get()`)**: Using `user.get("address", {}).get("city", "Not Available")` ensures your program never crashes with a `KeyError` if an API response omits a field.
- **HMAC-SHA256 Webhook Verification**:
  - Webhooks send events to your server. To ensure the sender is authentic and the data was not tampered with, the sender signs the payload with a shared secret key.
  - The receiver computes the HMAC hash of the payload using the secret.
  - **`hmac.compare_digest()`**: Performs a constant-time comparison. Never use standard `==` for cryptographic signatures, because `==` exits early on character mismatch, making it vulnerable to **timing attacks**!

### Tanglish:
- **`python-dotenv`**: Secret passwords and API keys-ah code kula direct-ah ezhudhama `.env` file-la vachu maraikka.
- **Retry Logic**: Namma call panra API server down-ah irundha udane fail aagama, automatic-ah 3 vaati retry panni recover aaga try pannum.
- **`.get()` safe navigation**: API-la oru data missing-ah irundha code crash aaga koodadhu nu fallback default value ("Not Available") thara `.get()` use panrom.
- **HMAC Signature Verification (Security)**:
  - Webhook moolama vara data genuine-ah illa hacker alter pannara nu check panna HMAC-SHA256 use panrom.
  - Signature compare panna epovume `hmac.compare_digest()` thaan use pannanum. Normal `==` use panna hackers timing attack moolama password-ah kandupidikka chance irukku!

```python
import hmac
import hashlib

def verify_signature(payload: str, signature: str, secret: str) -> bool:
    # 1. Compute expected hash using secret key and incoming payload
    expected_sig = hmac.new(
        key=secret.encode("utf-8"),
        msg=payload.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()

    # 2. Constant-time secure comparison
    return hmac.compare_digest(expected_sig, signature)
```

---

## 10. Weekly Assessment: FastAPI Microservice & Pytest

### English:
- **FastAPI**: Modern, high-performance web framework for building REST APIs.
- **Pydantic (`BaseModel`)**: Validates incoming request data (e.g., guarantees that an employee's name cannot be empty and salary must be strictly greater than 0). If validation fails, FastAPI automatically returns HTTP `422 Unprocessable Entity`.
- **Endpoints**:
  - `GET /health`: Server health probe.
  - `GET /employees`: Returns all employee records from `employees.json`.
  - `GET /employees/{name}`: Returns employee details or raises HTTP `404 Not Found`.
  - `POST /employees`: Creates a new record after validating input.
- **`pytest --cov=src`**: Runs automated unit tests to verify endpoints and measures test coverage (ensuring at least 80%+ of code lines are tested).

### Tanglish:
- **FastAPI**: Python-la romba fast-ana backend REST API create panra framework.
- **Pydantic**: User anuppura data sariya irukka nu check pannum (e.g. salary negative-ah irukka koodadhu, name empty-ah irukka koodadhu). Thappa irundha automatic-ah `422 Error` tharum.
- **API Endpoints**:
  - `/health`: Server nalla run aagudha nu check panna.
  - `/employees`: Ella employee data-vum eduka.
  - `POST /employees`: Pudhu employee-ah add panna.
- **`pytest`**: Namma ezhudhina code ellam sariya vela seiyudha nu test run panni 80%+ coverage kaatta use aagum.

---

## 🎯 Summary Checklist (நினைவில் வைக்க வேண்டியவை)

1. **Clean Code**: Never hardcode credentials; use `.env` and load via `python-dotenv`.
2. **Defensive Coding**: Use `.get(key, default)` and `try/except` so programs never crash unexpectedly.
3. **Security**: Always use `hmac.compare_digest()` for signatures to prevent timing attacks.
4. **Data Hygiene**: Always drop duplicates and impute null values with median/mean before analyzing.
5. **Git Discipline**: Keep `.env`, `.venv`, and `__pycache__` inside `.gitignore`.
