days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

print(sum(day['revenue'] for day in days))

days_revenue = {day["day"]: day["revenue"] for day in days}

print(max(days_revenue, key=days_revenue.get))

print({day["day"]: day["revenue"] / (day["orders"] - day["returns"]) for day in days})

print([day["day"] for day in days if day["returns"] / day["orders"] > 0.2])