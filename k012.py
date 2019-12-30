#! /usr/bin/python3
# coding: utf-8

date = input("日時(YYYY/MM/DD) : ").split("/")
year = int(date[0])
month = int(date[1])
day = int(date[2])

if month <= 2:
    month += 12

C = (year - 1) // 100
Y = (year - 1) % 100
F = day + (26*(month+1)/10) + int(Y) + (int(Y)/4) - 2*int(C) + (int(C)/4)
X = int(F % 7)
week = ["土", "日", "月", "火", "水", "木", "金"]
print("{year}年{month}月{day}日は「{week}」です．".format(year=year, month=month, day=day, week=week[X]))
