#! /usr/bin/python3
# coding: utf-8

import os.path
import re
import sys


def main():
    path = os.path.join(os.path.dirname(__file__), "k04x")

    files = sys.argv
    outputs = []
    pattern = '<dt>(.*?)\\((.*?)所属\\)</dt>.*?<dd>(.*?)</dd>'

    if not os.path.isfile(os.path.join(path, files[1])):
        print(files[1] + ": No such file or directory.")
        exit(1)

    with open(os.path.join(path, files[1]), encoding="utf-8", mode="r") as file:
        html = file.read()
        results = re.findall(pattern, html, re.S)

        for result in results:
            # [author, department, research]
            outputs.append("{department},{author},{research}"
                           .format(author=result[0], department=result[1], research=result[2]))

    with open(os.path.join(path, files[2]), encoding="utf-8", mode="w", newline="\n") as file:
        for output in outputs:
            file.write(output + "\n")


if __name__ == '__main__':
    main()
