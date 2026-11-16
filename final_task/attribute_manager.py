def add_attribute(data, attr_name, derive_fn):
    for row in data:
        row[attr_name] = derive_fn(row)
    return data


def flatten_laureates_and_prizes(laureates):
    flattened = []
    for laureate in laureates:
        prizes = laureate.get("prizes_relevant") or []
        if not prizes:
            flat_row = {
                "id": laureate.get("id"),
                "name": laureate.get("name"),
                "gender": laureate.get("gender"),
                "type_": laureate.get("type_"),
                "birth_year": laureate.get("birth_year"),
                "country_birth": laureate.get("country_birth"),
                "country_now": laureate.get("country_now"),
                "founded_year": laureate.get("founded_year"),
                "country_founded": laureate.get("country_founded"),
                "award_year": None,
                "category_en": None,
                "prize_amount": None,
                "prize_amount_adjusted": None,
                "prize_status": None,
                "num_prizes": 0,
            }
            flattened.append(flat_row)
            continue

        for prize in prizes:
            flat_row = {
                "id": laureate.get("id"),
                "name": laureate.get("name"),
                "gender": laureate.get("gender"),
                "type_": laureate.get("type_"),
                "birth_year": laureate.get("birth_year"),
                "country_birth": laureate.get("country_birth"),
                "country_now": laureate.get("country_now"),
                "founded_year": laureate.get("founded_year"),
                "country_founded": laureate.get("country_founded"),
                "award_year": prize.get("award_year"),
                "category_en": prize.get("category_en"),
                "prize_amount": prize.get("prize_amount"),
                "prize_amount_adjusted": prize.get("prize_amount_adjusted"),
                "prize_status": prize.get("prize_status"),
                "num_prizes": len(prizes),
            }
            flattened.append(flat_row)
    return flattened


if __name__ == "__main__":
    sample_laureates = [
        {
            "id": "1",
            "name": "Linus Pauling",
            "gender": "male",
            "type_": "person",
            "birth_year": 1901,
            "country_birth": "USA",
            "country_now": "USA",
            "prizes_relevant": [
                {"award_year": 1954, "category_en": "Chemistry", "prize_amount": 1000},
                {"award_year": 1962, "category_en": "Peace", "prize_amount": 2000},
            ],
        },
        {
            "id": "2",
            "name": "Empty Org",
            "gender": None,
            "type_": "org",
            "founded_year": 2000,
            "country_founded": "Geneva",
            "country_now": "Switzerland",
            "prizes_relevant": [],
        },
    ]

    flat = flatten_laureates_and_prizes(sample_laureates)
    assert len(flat) == 3
    assert flat[0]["category_en"] == "Chemistry"
    assert flat[1]["category_en"] == "Peace"
    assert flat[2]["award_year"] is None
    assert flat[2]["num_prizes"] == 0

    add_attribute(flat, "is_us", lambda r: r["country_now"] == "USA")
    assert flat[0]["is_us"] is True
    assert flat[2]["is_us"] is False

    print("Всё прошло успешно!")