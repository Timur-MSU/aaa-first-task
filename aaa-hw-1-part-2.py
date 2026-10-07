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
print(len(queries))

from collections import Counter

print(dict(Counter(queries)))

counter_queries = dict(Counter(queries))
print(max(counter_queries, key=counter_queries.get))

print(max(counter_queries.values()) / len(queries))

print([query for query, count in counter_queries.items() if count == 1])