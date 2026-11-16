import pandas as pd

# 1. Load and clean orders
orders = pd.read_csv("orders.csv").drop_duplicates()
orders["amount"] = pd.to_numeric(orders["amount"])
orders["amount"] = orders["amount"].fillna(orders["amount"].median())
orders["order_id"] = orders["order_id"].astype(str)

# 2. Load customers
customers = pd.read_csv("customers.csv")

# 3. Inner Join
inner_df = pd.merge(orders, customers, on="customer_id", how="inner")
print(f"Inner join rows: {len(inner_df)} (customer 104 dropped)")

# 4. Left Join from customers (find customers with no orders)
left_df = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = left_df[left_df["order_id"].isna()]["name"].tolist()
print(f"No orders: {', '.join(no_orders)}")

# 5. Outer Join (find order without customer record)
outer_df = pd.merge(orders, customers, on="customer_id", how="outer", indicator=True)
no_customer = outer_df[outer_df["_merge"] == "left_only"]["customer_id"].tolist()
print(f"Order without customer: customer_id {', '.join(map(str, no_customer))}")

# 6. When to use each join type:
# Inner Join: When you only want records that exist in both tables.
# Left Join: When you need all records from the primary table, even if unmatched.
# Outer Join: When you need complete data from both tables to identify missing links.
