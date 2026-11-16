# 1. apply_discount with default discount=10
def apply_discount(price, discount=10):
    return float(price - (price * discount / 100))


# 2. total(*args) and describe(**kwargs)
def total(*args):
    return sum(args)


def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Test function calls
print(f"apply_discount(1000) -> {apply_discount(1000)}")
print(f"apply_discount(1000, 25) -> {apply_discount(1000, 25)}")
print(f"total(5, 10, 15) -> {total(5, 10, 15)}")

# 3. List comprehension: prices above 1000
prices = [500, 1200, 800, 2500, 300]
above_1000 = [p for p in prices if p > 1000]
print(f"Above 1000: {above_1000}")

# 4. map() with lambda: add 18% GST rounded to 2 decimals
with_gst = list(map(lambda p: round(p * 1.18, 2), prices))
print(f"With GST: {with_gst}")

# 5. filter(): keep prices below 1000
below_1000 = list(filter(lambda p: p < 1000, prices))
print(f"Below 1000: {below_1000}")
