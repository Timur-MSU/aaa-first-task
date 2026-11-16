from json_dict_processing import create_processor


def process_award_year(year_val):
    if year_val is None:
        return None
    try:
        return int(year_val)
    except (ValueError, TypeError):
        return None


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], process_award_year),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
}


def prize_processor():
    return create_processor(CONFIG_PRIZE, list_processor=True)


if __name__ == "__main__":
    test_raw_prizes = [
        {
            "awardYear": "2001",
            "category": {"en": "Economic Sciences"},
            "prizeAmount": 10000000,
            "prizeAmountAdjusted": 15547541,
            "prizeStatus": "received",
        }
    ]

    proc = prize_processor()
    processed = proc(test_raw_prizes)

    assert len(processed) == 1
    assert processed[0]["award_year"] == 2001
    assert processed[0]["category_en"] == "Economic Sciences"
    assert processed[0]["prize_amount"] == 10000000

    print("Файл prizes_configs.py работает корректно!")
