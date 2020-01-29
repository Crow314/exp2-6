#! /usr/bin/python3
# coding: utf-8

import random
import os.path


def main():
    path = os.path.join(os.path.dirname(__file__), "k02x")
    year = "2015"
    month = "Aug"

    record_style = "{0}/{1}/{2:02d}\t{3:2.3f}"

    with open(os.path.join(path, "temperature.dat"), encoding="utf-8", mode="w") as file:
        file.write("年/月/日\t\t気温［℃］" + "\n")

        for day in range(1, 31+1):
            random.seed()
            temperature = random.uniform(30.0, 40.0)

            file.write(record_style.format(year, month, day, temperature) + "\n")


if __name__ == '__main__':
    main()
