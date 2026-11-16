# 1. Variables of every type and their type()
var_int = 42
var_float = 3.14
var_str = "Hello Python"
var_list = [10, 20, 30]
var_dict = {"name": "Arun", "role": "Developer"}
var_set = {1, 2, 3}
var_tuple = (100, 200)

types_data = [
    ("int", var_int),
    ("float", var_float),
    ("str", var_str),
    ("list", var_list),
    ("dict", var_dict),
    ("set", var_set),
    ("tuple", var_tuple),
]

for type_name, value in types_data:
    print(f"{type_name}: {value} -> {type(value)}")

print("-" * 40)

# 2. Sales Report Loop
sales = [12000, 0, 8500, 15000, -200, 9800]
total = 0

for sale in sales:
    if sale <= 0:
        print(f"Skipped invalid value {sale}")
        continue

    total += sale
    print(f"Added {sale} total {total}")

    if total > 30000:
        break

# 3. Check target reached
if total > 30000:
    print(f"Target reached. Stopped at {total}")
else:
    print(f"Target not reached. Total: {total}")
