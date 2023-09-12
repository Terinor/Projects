from datetime import date
import main
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch


# Приклад використання:
users = [
    {"name": "wrong_previous", "birthday": date(2000, 2, 15)},
    {"name": "wright_mondey", "birthday": date(1995, 2, 16)},
    {"name": "mondey", "birthday": date(2000, 2, 20)},
    {"name": "wensday", "birthday": date(2000, 2, 24)},
    {"name": "saturday", "birthday": date(2000, 2, 25)},

    {"name": "wrong_next", "birthday": date(1988, 2, 21)}
]

birthdays = main.get_birthdays_per_week(users)
print(birthdays)

users = [
    {"name": "wrong_previous", "birthday": date(2000, 9, 15)},
    {"name": "wright_mondey", "birthday": date(1995, 9, 16)},
    {"name": "wednesday", "birthday": date(2000, 9, 20)},
    {"name": "wensday", "birthday": date(2000, 9, 24)},
    {"name": "saturday", "birthday": date(2000, 9, 25)},

    {"name": "wrong_next", "birthday": date(1988, 10, 21)}
]

birthdays = main.get_birthdays_per_week(users)
print(birthdays)

users = [
            {
                "name": "John",
                "birthday": (self.today + timedelta(days=1)).date(),
            },
            {
                "name": "Doe",
                "birthday": (self.today + timedelta(days=3)).date(),
            },
            {"name": "Alice", "birthday": (self.today + timedelta(days=-3)).date()},
        ]

birthdays = main.get_birthdays_per_week(users)
print(birthdays)