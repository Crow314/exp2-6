#! /usr/bin/python3
# coding: utf-8


def main():
    start = input("開始日(YYYY/MM/DD) : ").split("/")
    finish = input("開始日(YYYY/MM/DD) : ").split("/")

    year_start = int(start[0])
    month_start = int(start[1])
    day_start = int(start[2])

    year_finish = int(finish[0])
    month_finish = int(finish[1])
    day_finish = int(finish[2])

    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    # day_start
    day += month_length[month_start-1] - day_start + 1
    if month_start == 2 & is_leap_year(year_start):  # 閏年
        day += 1
    month_start += 1

    # day_finish
    day += day_finish
    month_finish -= 1

    # month_start
    for month in range(month_start-1, 12):
        day += month_length[month_start-1]
        if month == 2 & is_leap_year(year_start):
            day += 1
    year_start += 1

    # month_finish
    for month in range(0, month_start-1):
        day += month_length[month_finish-1]
        if month == 2 & is_leap_year(year_start):
            day += 1
    year_finish -= 1

    # year
    for year in range(year_start + 1, year_finish):
        day += 365
        if is_leap_year(year):
            day += 1

    print("日数差:{day}日".format(day=day))


def is_leap_year(year):
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result


main()
