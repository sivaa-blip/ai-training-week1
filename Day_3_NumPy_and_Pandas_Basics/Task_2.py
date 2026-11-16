import pandas as pd

# 1. Load employees.csv
df = pd.read_csv("employees.csv")

# 2. DataFrame inspection methods
print("--- df.head() ---")
print(df.head())

print("\n--- df.info() ---")
df.info()

print("\n--- df.describe() ---")
print(df.describe())

# 3 lines explaining what each shows:
# df.head() previews the first 5 records of the dataset.
# df.info() displays column names, data types, and non-null counts.
# df.describe() computes statistical summaries (mean, std, min, quartiles, max).

# 3. Column selection
name_only = df["name"]
name_and_salary = df[["name", "salary"]]

# 4. loc for Chennai employees and iloc for slice
chennai_names = df.loc[df["city"] == "Chennai", "name"]
slice_data = df.iloc[0:3, 1:3]

# 5. Filtering counts
salary_above_50k = df[df["salary"] > 50000]
it_employees = df[df["department"] == "IT"]

print(f"Chennai: {', '.join(chennai_names)}")
print(f"Salary above 50000: {len(salary_above_50k)} employees")
print(f"IT department: {', '.join(it_employees['name'])}")
