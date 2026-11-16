import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

# 1. Bar Chart: Average salary per department
plt.figure(figsize=(8, 5))
avg_salary = df.groupby("department")["salary"].mean()
bars = plt.bar(
    avg_salary.index,
    avg_salary.values,
    color="skyblue",
    edgecolor="navy",
)
plt.bar_label(bars, fmt="%.0f")
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.savefig("bar_chart.png")
plt.close()

# 2. Histogram: Salary distribution with 5 bins
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, color="coral", edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.savefig("histogram.png")
plt.close()

# 3. Scatter Plot: ID vs Salary coloured by department with a legend
plt.figure(figsize=(8, 5))
for dept in df["department"].unique():
    group = df[df["department"] == dept]
    plt.scatter(group["id"], group["salary"], label=dept, s=80)
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.savefig("scatter_plot.png")
plt.close()

# 4. Line Chart: Monthly sales (Jan to Jun) with markers
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", color="green", linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("line_chart.png")
plt.close()

# Bonus Challenge: All four charts on one 2x2 figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Bar Chart
bars = axes[0, 0].bar(
    avg_salary.index, avg_salary.values, color="skyblue", edgecolor="navy"
)
axes[0, 0].bar_label(bars, fmt="%.0f")
axes[0, 0].set_title("Average Salary per Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")

# Subplot 2: Histogram
axes[0, 1].hist(df["salary"], bins=5, color="coral", edgecolor="black")
axes[0, 1].set_title("Salary Distribution (5 Bins)")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Number of Employees")

# Subplot 3: Scatter Plot
for dept in df["department"].unique():
    group = df[df["department"] == dept]
    axes[1, 0].scatter(group["id"], group["salary"], label=dept, s=60)
axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend(title="Department")

# Subplot 4: Line Chart
axes[1, 1].plot(months, sales, marker="o", color="green", linewidth=2)
axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")

plt.tight_layout()
plt.savefig("all_charts_combined.png")
plt.close()

print("All charts generated and saved successfully!")
