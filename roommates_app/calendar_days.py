import calendar
import collections

days_in_week = []
for month in range(1, 13):
    weeks_in_month = calendar.monthcalendar(2018, month)
    for week in weeks_in_month:
        days_in_week.append(week)

week_days = {}
week_number = []

for i in range(1,100):
    week_number.append(i)

week_with_weekdays = dict(zip(week_number, days_in_week))

sorted_week_with_weekdays = collections.OrderedDict(sorted(week_with_weekdays.items()))

for key, value in sorted_week_with_weekdays.items():
    print(key, value)
