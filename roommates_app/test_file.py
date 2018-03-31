import datetime

first_week_of_the_month = datetime.date.today().isocalendar()[1]
last_week_of_two_months = first_week_of_the_month + 9

all_range = list(range(first_week_of_the_month, last_week_of_two_months + 1))
print(all_range)