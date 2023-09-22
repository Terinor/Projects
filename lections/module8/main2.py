from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    next_week_birthday = {day: [] for day in weekdays}

    for user in users:
        name = user['name']
        birthday_this_year = date(today.year, user['birthday'].month, user['birthday'].day)
        
        if birthday_this_year < today:
            continue  # Skip if the birthday has already passed this year

        delta_days = (birthday_this_year - today).days
        if delta_days > 6:
            continue  # Skip if the birthday is more than one week away

        weekday_name = birthday_this_year.strftime("%A")
        
        if weekday_name in ["Saturday", "Sunday"]:
            weekday_name = "Monday"  # Move weekend birthdays to Monday
        
        next_week_birthday[weekday_name].append(name)
    
    # Remove empty lists
    return {k: v for k, v in next_week_birthday.items() if v}

# Example usage:
users = [
    {"name": "wrong_previous", "birthday": date(2000, 9, 15)},
    {"name": "wright_mondey", "birthday": date(1995, 9, 17)},
    {"name": "wednesday", "birthday": date(2000, 9, 20)},
    {"name": "wensday", "birthday": date(2000, 9, 24)},
    {"name": "saturday", "birthday": date(2000, 9, 25)},

    {"name": "wrong_next", "birthday": date(1988, 10, 21)}
]

print(get_birthdays_per_week(users))
