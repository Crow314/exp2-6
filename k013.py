#! /usr/bin/python3
# coding: utf-8

import calendar


def main():
    date = input("日時(YYYY/MM) : ").split("/")
    year = int(date[0])
    month = int(date[1])

    print(MyCalendar(calendar.SUNDAY).formatmonth(year, month))


class MyCalendar(calendar.TextCalendar):

    def formatmonthname(self, theyear, themonth, width, withyear=True):
        s = str(themonth) + "月"
        if withyear:
            s = "%r年 %s" % (theyear, s)
        return s.center(width)

    def formatweekday(self, day, width):
        """
        Returns a formatted week day name.
        """
        # width -= 1
        if width >= 9:
            names = ["月", "火", "水", "木", "金", "土", "日"]
        else:
            names = ["月", "火", "水", "木", "金", "土", "日"]
        return names[day][:width].center(width)


main()
