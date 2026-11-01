from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]


def main():
    print("Всего поисковых запросов в ленте:", len(queries))

    counter_queries = dict(Counter(queries))
    print("Сколько раз ввели каждый запрос:", counter_queries)

    print("Запрос, который вводили чаще всего:", max(counter_queries, key=counter_queries.get))
    print("Какую долю всех поисков он занимает:", max(counter_queries.values()) / len(queries))
    print("Запросы, встретившиеся один раз:", [query for query, count in counter_queries.items() if count == 1])


if __name__ == "__main__":
    main()
