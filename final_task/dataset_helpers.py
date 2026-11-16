from collections import defaultdict


def filter_data(data, predicate):
    if not data:
        return []
    return [row for row in data if predicate(row)]


def group_by_attributes(data, keys):
    if isinstance(keys, str):
        keys = [keys]

    grouped = defaultdict(list)
    for row in data:
        group_key = tuple(row.get(k) for k in keys)
        if len(keys) == 1:
            group_key = group_key[0]
        grouped[group_key].append(row)

    return dict(grouped)


if __name__ == "__main__":
    sample = [
        {"name": "Alice", "country": "USA", "age": 25},
        {"name": "Bob", "country": "UK", "age": 30},
        {"name": "Charlie", "country": "USA", "age": 25},
    ]

    filtered = filter_data(sample, lambda r: r["age"] < 30)
    assert len(filtered) == 2
    assert filter_data([], lambda r: True) == []

    grouped_single = group_by_attributes(sample, "country")
    assert len(grouped_single["USA"]) == 2
    assert len(grouped_single["UK"]) == 1

    grouped_multi = group_by_attributes(sample, ["country", "age"])
    assert len(grouped_multi[("USA", 25)]) == 2

    print("Все тесты dataset_helpers.py успешно пройдены!")
