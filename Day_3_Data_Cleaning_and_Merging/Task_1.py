import pandas as pd

# 1. Load orders.csv
df = pd.read_csv("orders.csv")

# 2. Find missing values and duplicates
missing_amount = df["amount"].isna().sum()
duplicates = df.duplicated().sum()
print(f"Missing: amount {missing_amount} | Duplicates: {duplicates}")

# 3. Remove duplicate row
df = df.drop_duplicates()

# 4. Make sure amount is numeric and fill missing with median
df["amount"] = pd.to_numeric(df["amount"])
median_val = df["amount"].median()
df["amount"] = df["amount"].fillna(median_val)
print(f"Median used: {median_val}")

# 5. Make sure order_id is a string
df["order_id"] = df["order_id"].astype(str)

# 6. Group by customer_id and aggregate
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print(result)
