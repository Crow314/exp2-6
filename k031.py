#! /usr/bin/python3
# coding: utf-8

import os.path
import sys


def main():
    path = os.path.join(os.path.dirname(__file__), "k03x")

    file_original = sys.argv[1]
    file_generate = sys.argv[2]

    if not os.path.isfile(os.path.join(path, file_original)):
        print(file_original + ": No such file or directory.")
        exit(1)

    lines = []
    with open(os.path.join(path, file_original), encoding="utf-8", mode="r") as file:
        for line in file:
            lines.append(line)

    lines = list(set(lines))

    with open(os.path.join(path, file_generate), encoding="utf-8", mode="w", newline="\n") as file:
        for line in lines:
            file.write(line)


if __name__ == '__main__':
    main()
