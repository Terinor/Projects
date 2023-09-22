from datetime import date, datetime, timedelta
from this_week import is_birthday_next_week, is_birthday_this_week_or_last_weekend, is_in_next_7_days


def get_birthdays_per_week(users):
    birthdays_next_week = {}
    today = date.today()
    next_week = today + timedelta(days=7)

    for user in users:
        birthday_this_year = user['birthday'].replace(year=today.year)
        birthday_next_year = user['birthday'].replace(year=today.year + 1)
        birthday = user['birthday']
        # Choose the appropriate birthday year
        birthday_to_check = birthday_next_year if next_week.year > today.year else birthday_this_year

        if is_in_next_7_days(birthday_this_year) or is_in_next_7_days(birthday_next_year):
            weekday_name = date.strftime(birthday, '%A')
            
            if weekday_name in ['Saturday', 'Sunday']:
                weekday_name = 'Monday'

            if weekday_name not in birthdays_next_week:
                birthdays_next_week[weekday_name] = []

            birthdays_next_week[weekday_name].append(user['name'])

    return birthdays_next_week


if __name__ == "__main__":
    users = [
        {"name": "wrong_previous", "birthday": date(2000, 9, 15)},
        {"name": "saturday", "birthday": date(1995, 9, 23)},
        {"name": "wedn2esday", "birthday": date(2000, 9, 27)},
        {"name": "wen2sday", "birthday": date(2000, 9, 21)},
        {"name": "mondey", "birthday": date(2001, 9, 25)},
        {"name": "wrong_next", "birthday": date(1988, 10, 21)}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")