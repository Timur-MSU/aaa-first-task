def extract_nested_value(obj, keys):
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current


def process_dictionary_with_config(dictionary, config):
    new_dictionary = {}

    for target_field, rule in config.items():
        if isinstance(rule, tuple):
            path, func = rule
        else:
            path, func = rule, None

        value = extract_nested_value(dictionary, path)

        if func is not None and value is not None:
            value = func(value)

        new_dictionary[target_field] = value

    return new_dictionary


def process_list_of_dicts_with_config(list_of_dicts, config):
    if list_of_dicts is None or list_of_dicts == []:
        return []
    result = []
    for dictionary in list_of_dicts:
        processed_item = process_dictionary_with_config(dictionary, config)
        result.append(processed_item)
    return result


def create_processor(config, list_processor=False):
    if list_processor:
        def processor(data):
            return process_list_of_dicts_with_config(data, config)

        return processor
    else:
        def processor(data):
            return process_dictionary_with_config(data, config)

        return processor


if __name__ == "__main__":
    test_raw_data = {
        "id": "101",
        "person": {
            "name": {"first": "Marie", "last": "Curie"},
            "birth": {"year": "1867"},
        },
        "tags": None,
    }

    assert extract_nested_value(test_raw_data, ["person", "name", "first"]) == "Marie"
    assert extract_nested_value(test_raw_data, ["person", "missing_field"]) is None
    assert extract_nested_value(test_raw_data, ["tags", "subtag"]) is None

    test_config = {
        "first_name": ["person", "name", "first"],
        "birth_year": (["person", "birth", "year"], int),
        "death_year": ["person", "death", "year"],
    }

    processed = process_dictionary_with_config(test_raw_data, test_config)
    assert processed == {
        "first_name": "Marie",
        "birth_year": 1867,
        "death_year": None,
    }

    processor = create_processor(test_config, list_processor=False)
    assert processor(test_raw_data) == processed

    print("Всё прошло успешно!")
