#! /usr/bin/python3
# coding: utf-8

import os.path
import sys


def main():
    path = os.path.join(os.path.dirname(__file__), "k03x")

    files = sys.argv
    outputs = []

    for file_name in files[1:-1]:
        if not os.path.isfile(os.path.join(path, file_name)):
            print(file_name + ": No such file or directory.")
            exit(1)

        words = []
        character_count = 0
        line_count = 0

        with open(os.path.join(path, file_name), encoding="utf-8", mode="r") as file:
            for line in file:
                for word in line.split():
                    words.append(word)
                line.replace(" ", "")
                line.replace("\n", "")
                character_count += len(line)
                line_count += 1

        # words = list(set(words))
        word_count = len(words)
        outputs.append("{0}: {1}文字， {2}語， {3}行".format(file_name, character_count, word_count, line_count))

        with open(os.path.join(path, files[-1]), encoding="utf-8", mode="w", newline="\n") as file:
            for output in outputs:
                file.write(output + "\n")


if __name__ == '__main__':
    main()
