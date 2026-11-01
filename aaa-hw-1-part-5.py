reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]


def main():
    for review in reviews:
        review["product"] = review["product"].capitalize()

    stats = {}
    for review in reviews:
        product = review["product"]
        stars = review["stars"]

        if product not in stats:
            stats[product] = {"sum_stars": 0, "count": 0}

        stats[product]["sum_stars"] += stars
        stats[product]["count"] += 1

    print(
        "Средняя оценка каждого товара:",
        {product: stat["sum_stars"] / stat["count"] for product, stat in stats.items()},
    )

    avg_stats_where_2_and_more_reviews = {
        product: stat["sum_stars"] / stat["count"]
        for product, stat in stats.items()
        if stat["count"] > 1
    }
    print(
        "Худший товар по средней оценке среди тех, у кого хотя бы два отзыва:",
        min(avg_stats_where_2_and_more_reviews, key=avg_stats_where_2_and_more_reviews.get),
    )

    count_1_2_star = 0
    for review in reviews:
        if review["stars"] in (1, 2):
            count_1_2_star += 1

    print("Сколько отзывов на 1 или 2 звезды:", count_1_2_star)
    print("Какую долю всех отзывов они составляют:", count_1_2_star / len(reviews))


if __name__ == "__main__":
    main()
