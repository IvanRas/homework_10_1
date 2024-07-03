from typing import Any

inform_state = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(inform_state: list[dict[str]], state='CANCELED') -> Any:
    """Функция фильтрации по ключу state"""
    list_state = []
    for key in inform_state:
        if key.get("state") == state:
            list_state.append(key)
    return list_state


print(filter_by_state(inform_state))