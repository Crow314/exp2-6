#! /usr/bin/python3
# coding: utf-8

import datetime


def main():
    start = input("開始日(YYYY/MM/DD) : ").split("/")
    finish = input("終了日(YYYY/MM/DD) : ").split("/")

    year_start = int(start[0])
    month_start = int(start[1])
    day_start = int(start[2])

    year_finish = int(finish[0])
    month_finish = int(finish[1])
    day_finish = int(finish[2])

    date_start = datetime.date(year_start, month_start, day_start)
    date_finish = datetime.date(year_finish, month_finish, day_finish)
    print("日数差 : {dif}日".format(dif=(date_finish-date_start).days))


main()
