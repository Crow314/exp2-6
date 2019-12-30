#! /usr/bin/python3
# coding: utf-8

year = int(input("何年(YYYY) : "))

leapYear = False

if year % 400 == 0:
    leapYear = True
elif year % 100 == 0:
    leapYear = False
elif year % 4 == 0:
    leapYear = True

leapStr = "閏年" if leapYear else "平年"
print("{year}年は「{leap}」です．".format(year=year, leap=leapStr))
