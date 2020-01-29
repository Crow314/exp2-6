#! /usr/bin/python3
# coding: utf-8

import os.path


def main():
    path = os.path.join(os.path.dirname(__file__), "k02x")

    n = 0
    total = 0.0
    temperature_max = 0.0
    temperature_min = 100.0
    date_max = 0
    date_min = 0

    if not os.path.isfile(os.path.join(path, "temperature.dat")):
        print("temperature.dat: No such file or directory.")
        exit(1)

    with open(os.path.join(path, "temperature.dat"), encoding="utf-8", mode="r") as file:
        for line in file:
            daily_data = line.split()
            if daily_data[1] == "気温［℃］":
                continue

            temperature = float(daily_data[1])

            if temperature_max < temperature:
                temperature_max = temperature
                date_max = daily_data[0]

            if temperature_min > temperature:
                temperature_min = temperature
                date_min = daily_data[0]

            total = total + temperature
            n += 1

    average = total / n

    with open(os.path.join(path, "average.dat"), encoding="utf-8", mode="w") as file:
        file.write("日時：{0}，最高気温：{1:2.3f} ℃".format(date_max, temperature_max) + "\n")
        file.write("日時：{0}，最低気温：{1:2.3f} ℃".format(date_min, temperature_min) + "\n")
        file.write("平均気温：{0:2.3f} ℃".format(average) + "\n")


if __name__ == '__main__':
    main()
