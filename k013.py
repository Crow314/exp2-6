#! /usr/bin/python3
# coding: utf-8


def main():
    date = input("日時(YYYY/MM) : ").split("/")
    year = int(date[0])
    month = int(date[1])
    day = 1
    print("    {year} 年 {month} 月".format(year=year, month=month))
    week = ["日", "月", "火", "水", "木", "金", "土"]
    for day_of_week in week:
        print(day_of_week, "", end="")

    day_of_week = zeller(year, month, day)
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_length[month-1]
    if month == 2:
        if is_leap_year(year):
            days += 1

    for i in range(1, days+1):



def zeller(year, month, day):
    if month <= 2:
        month += 12

    c = (year - 1) // 100
    y = (year - 1) % 100
    f = day + (26*(month+1)/10) + int(y) + (int(y)/4) - 2*int(c) + (int(c)/4)
    x = int(f % 7)
    x = (x-1) % 7
    return x


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
