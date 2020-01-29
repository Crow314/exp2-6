#! /usr/bin/python3
# coding: utf-8

import os.path


def main():
    path = os.path.join(os.path.dirname(__file__), "k02x")

    file = input("Data file:")

    if not os.path.isfile(os.path.join(path, file)):
        print(file + ": No such file or directory.")
        exit(1)

    rule = int(input("Rule (昇順:0, 降順:1):"))
    temperatures = []

    with open(os.path.join(path, "temperature.dat"), encoding="utf-8", mode="r") as file:
        for line in file:
            daily_data = line.split()
            if daily_data[1] == "気温［℃］":
                continue

            temperatures.append({"date": daily_data[0], "temperature": float(daily_data[1])})

    temperatures_sorted = {}
    if rule == 0:
        temperatures_sorted = sorted(temperatures, key=lambda x: x["temperature"])
    if rule == 1:
        temperatures_sorted = sorted(temperatures, reverse=True, key=lambda x: x["temperature"])

    n = 1
    for daily_data in temperatures_sorted:
        print("{0}:\t{1}\t{2:2.3f}".format(n, daily_data["date"], daily_data["temperature"]))
        n += 1


if __name__ == '__main__':
    main()
