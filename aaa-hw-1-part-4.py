days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]


def main():
    print("Выручка за всю неделю:", sum(day["revenue"] for day in days))

    days_revenue = {day["day"]: day["revenue"] for day in days}
    print("День с самой большой выручкой:", max(days_revenue, key=days_revenue.get))

    print(
        "Средняя выручка на один заказ в каждый день:",
        {day["day"]: day["revenue"] / day["orders"] for day in days},
    )

    print(
        "Дни, где возвратов больше 20% заказов:",
        [day["day"] for day in days if day["returns"] / day["orders"] > 0.2],
    )


if __name__ == "__main__":
    main()
