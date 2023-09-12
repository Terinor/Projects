from datetime import date, datetime
from this_week import is_birthday_next_week, is_birthday_this_week_or_last_weekend, this_week


def get_birthdays_per_week(users):
    
    birthdays_next_week = {}
    today = date.today()
    week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []        
    }
    
    for user in users:
        birthday = user['birthday']

        if this_week(birthday.replace(year=today.year)):
                        
            birthday_weekday = birthday.weekday()

            if birthday_weekday in [5, 6]:
                week['Monday'].append(user['name'])
                
            else:
                week[date.strftime(birthday, '%A')].append(user['name'])

        for key, value in week.items():
            if value != []:  
                birthdays_next_week[key] = value

    return birthdays_next_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
