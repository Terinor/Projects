from datetime import date, timedelta

def generate_next_7_dates():
    today = date.today()
    return [today + timedelta(days=i) for i in range(7)]

def same_day_and_month(date1, date2):
    return date1.day == date2.day and date1.month == date2.month

def get_birthdays_next_week(users):
    birthdays_next_week = {}
    dates_list = generate_next_7_dates()

    for user in users:
        for d in dates_list:
            if same_day_and_month(user['birthday'], d):
                weekday_name = d.strftime('%A')
                
                if weekday_name in ['Saturday', 'Sunday']:
                    weekday_name = 'Monday'

                if weekday_name not in birthdays_next_week:
                    birthdays_next_week[weekday_name] = []
                
                birthdays_next_week[weekday_name].append(user['name'])

    return birthdays_next_week

# Список користувачів
users = [
        {"name": "wrong_previous", "birthday": date(2000, 9, 15)},
        {"name": "saturday", "birthday": date(1995, 9, 23)},
        {"name": "wedn2esday", "birthday": date(2000, 9, 27)},
        {"name": "wen2sday", "birthday": date(2000, 9, 21)},
        {"name": "mondey", "birthday": date(2001, 9, 25)},
        {"name": "wrong_next", "birthday": date(1988, 10, 21)}
    ]



# Знаходимо дні народження на наступний тиждень
birthdays_next_week = get_birthdays_next_week(users)

# Виводимо результат
for weekday, names in birthdays_next_week.items():
    print(f"{weekday}: {', '.join(names)}")