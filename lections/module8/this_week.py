from datetime import date, timedelta



def is_birthday_this_week_or_last_weekend(birthday):
    today = date.today()
    
    current_weekday = today.weekday()
    
    last_saturday = today - timedelta(days=current_weekday+2)
    
    next_sunday = last_saturday + timedelta(days=8)
    
    return last_saturday <= birthday <= next_sunday


def is_birthday_next_week(birthday):
    today = date.today()

    current_weekday = today.weekday()

    next_saturday = today + timedelta(days=(5 - current_weekday))

    next_friday = next_saturday + timedelta(days=6)

    return next_saturday <= birthday <= next_friday

def this_week(your_date):

    # Get the current date
    current_date = date.today()

    # Calculate the year and week number for both dates
    your_year, your_week, _ = your_date.isocalendar()
    current_year, current_week, _ = current_date.isocalendar()

    # Check if the year and week match
    return your_year == current_year and your_week == current_week

def is_in_next_7_days(target_date):
    today = date.today()
    next_week = today + timedelta(days=7)
    
    return today <= target_date <= next_week
