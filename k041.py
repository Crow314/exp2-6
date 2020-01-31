#! /usr/bin/python3
# coding: utf-8

import os.path
import sys


def main():
    path = os.path.join(os.path.dirname(__file__), "k04x")

    files = sys.argv
    outputs = []

    if not os.path.isfile(os.path.join(path, files[1])):
        print(files[1] + ": No such file or directory.")
        exit(1)

    with open(os.path.join(path, files[1]), encoding="utf-8", mode="r") as file:
        for line in file:
            # [department, author, research]
            line_splitted = line.split(",")
            line_splitted[0] = line_splitted[0].replace("研", "研究室")
            output = "<dt>{author}({department}所属)</dt><dd>{research}</dd>"\
                .format(department=line_splitted[0], author=line_splitted[1], research=line_splitted[2])
            outputs.append(output.replace("\n", ""))

    with open(os.path.join(path, files[2]), encoding="utf-8", mode="w", newline="\n") as file:
        file.write('<!DOCTYPE HTML>\n'
                   '<html lang="ja">\n'
                   '\t<head>\n'
                   '\t\t<meta charset="UTF-8">\n'
                   '\t\t<title>研究一覧</title>\n'
                   '\t</head>\n'
                   '\t<body>\n'
                   '\t\t<dl>\n')
        for output in outputs:
            file.write('\t\t\t' + output + "\n")
        file.write('\t\t</dl>\n'
                   '\t</body>\n'
                   '</html>\n')


if __name__ == '__main__':
    main()
