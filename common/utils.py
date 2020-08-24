from datetime import datetime
import math


def get_remaining_days_until_saturday(date=None):
    ''' Get remaining days until saturday '''
    saturday_day_of_week = 5
    today_day_of_week = datetime.today().weekday() if date is None else date

    remaining_days = saturday_day_of_week - today_day_of_week
    return remaining_days if remaining_days is not 0 else 1


def get_remaining_proposes_per_day(current_proposes: int):
    ''' Calculate how much proposes per day do you have '''
    proposes_of_today = current_proposes / get_remaining_days_until_saturday()
    return int(math.floor(proposes_of_today))
