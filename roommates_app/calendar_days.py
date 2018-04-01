import calendar
from operator import itemgetter

month_number = list(range(1, 13))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

weeks_in_year = []
days_in_year = []
counter = 1

for j in range(1, 13):
    weeks_in_month = calendar.monthcalendar(2018, j)
    new_month = []
    for week in weeks_in_month:
        new_week = []
        for day in week:
            day_and_index = []
            day_and_index.append(counter)
            day_and_index.append(day)
            # if day != 0:
            #     counter += 1
            counter += 1
            new_week.append(day_and_index)
        new_month.append(new_week)
    weeks_in_year.append(new_month)
# for item in weeks_in_year:
#     print(item)


# for counter, value in enumerate(days_in_year):
#     print(counter, value)

# numbered_days = []
# counter = 1
# for day in days_in_year:
#     day_and_index = []
#     if day != 0:
#         day_and_index.append(counter)
#         day_and_index.append(day)
#         counter += 1
#     else:
#         day_and_index.append(counter)
#         day_and_index.append(day)
#     numbered_days.append(day_and_index)
#
# weeks = []
# seven_days = []
# for item in numbered_days:
#
#     seven_days.append(item)
#     if len(seven_days) ==7:
#         weeks.append(seven_days)
#         seven_days = []
#
# print(weeks)


# print(days_in_year)


    # new_weeks_in_month = []
    # for week in weeks_in_month:
    #     new_week = []
    #     for day in week:
    #         day_and_index = []
    #         day_and_index.append(counter)
    #         day_and_index.append(day)
    #         if day != 0:
    #             counter += 1
    #         # print(day_and_index)
    #         new_week.append(day_and_index)
    #     new_weeks_in_month.append(new_week)
    # weeks_in_year.append(new_weeks_in_month)



all_months_info = []

for i in range(0, 12):
    single_month_info = {}
    single_month_info.update({'number': month_number[i], 'month_name': months[i], 'weeks_in_month': weeks_in_year[i]})
    all_months_info.append(single_month_info)

sorted_all_month_info = sorted(all_months_info, key=itemgetter('number'))

