import statistics


def calculate_metric(rows, metric_field, heuristic='mean'):
    values = [row[metric_field] for row in rows if row.get(metric_field) is not None]

    if not values:
        return None

    if heuristic == 'count':
        return len(values)
    elif heuristic == 'mean':
        return round(statistics.mean(values), 2)
    elif heuristic == 'median':
        return round(statistics.median(values), 2)
    elif heuristic == 'sum':
        return sum(values)
    elif heuristic == 'min':
        return min(values)
    elif heuristic == 'max':
        return max(values)
    else:
        raise ValueError()


def get_top_n(items, key_func=lambda x: x[1], n=5, reverse=True):
    if isinstance(items, dict):
        items = list(items.items())
    return sorted(items, key=key_func, reverse=reverse)[:n]


if __name__ == "__main__":
    test_rows = [
        {"val": 10},
        {"val": 20},
        {"val": 30},
        {"val": None},
    ]

    assert calculate_metric(test_rows, "val", "mean") == 20.0
    assert calculate_metric(test_rows, "val", "median") == 20.0
    assert calculate_metric(test_rows, "val", "sum") == 60
    assert calculate_metric(test_rows, "val", "count") == 3
    assert calculate_metric(test_rows, "val", "min") == 10
    assert calculate_metric(test_rows, "val", "max") == 30
    assert calculate_metric([], "val", "mean") is None

    test_dict = {"USA": 300, "UK": 100, "Germany": 80, "France": 60, "Japan": 25}
    top_2 = get_top_n(test_dict, n=2)
    assert top_2 == [("USA", 300), ("UK", 100)]

    smallest_2 = get_top_n(test_dict, n=2, reverse=False)
    assert smallest_2 == [("Japan", 25), ("France", 60)]

    print("Все тесты aggregations.py успешно пройдены!")
