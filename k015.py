#! /usr/bin/python3
# coding: utf-8

import datetime


def main():
    start = input("開始時間(HH:MM) : ").split(":")
    finish = input("終了時間(HH:MM) : ").split(":")

    hour_start = int(start[0])
    min_start = int(start[1])

    hour_finish = int(finish[0])
    min_finish = int(finish[1])

    year = 2020
    month = 1
    day = 15

    time_start = datetime.datetime(year, month, day, hour_start, min_start)
    time_finish = datetime.datetime(year, month, day, hour_finish, min_finish)

    if time_start > time_finish:
        time_finish += datetime.timedelta(days=1)

    dif_hour = int((time_finish - time_start).total_seconds() // 3600)
    dif_min = int((time_finish - time_start).total_seconds() % 3600 // 60)

    print("経過時間 : {dif_hour}時間 {dif_min}分".format(dif_hour=dif_hour, dif_min=dif_min))


main()
