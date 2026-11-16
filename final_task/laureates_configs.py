from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string):
    try:
        return int(year_string[:4])
    except (ValueError, TypeError):
        return None


_prize_proc = prize_processor()

CONFIG_PERSON = {
    'id': ['id'],
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], _prize_proc),
}

CONFIG_ORG = {
    'id': ['id'],
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], _prize_proc),
}


def person_processor():
    return create_processor(CONFIG_PERSON, list_processor=False)


def org_processor():
    return create_processor(CONFIG_ORG, list_processor=False)

process_persons = person_processor()
process_orgs = org_processor()

if __name__ == "__main__":
    test_raw_person = {
        "id": "745",
        "knownName": {"en": "A. Michael Spence"},
        "gender": "male",
        "birth": {
            "date": "1943-11-07",
            "place": {
                "country": {"en": "USA"},
                "countryNow": {"en": "USA"},
            },
        },
        "nobelPrizes": [
            {
                "awardYear": "2001",
                "category": {"en": "Economic Sciences"},
                "prizeAmount": 10000000,
                "prizeAmountAdjusted": 15547541,
                "prizeStatus": "received",
            }
        ],
    }

    res = process_persons(test_raw_person)
    assert res["name"] == "A. Michael Spence"
    assert res["birth_year"] == 1943
    assert res["country_birth"] == "USA"
    assert len(res["prizes_relevant"]) == 1
    assert res["prizes_relevant"][0]["award_year"] == 2001

    print("Файл laureates_configs.py работает корректно!")