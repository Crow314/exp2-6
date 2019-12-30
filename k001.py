#! /usr/bin/python3
# coding: utf-8

print("   | ", end="")

for i in range(1, 10):
    print("{num:>2} ".format(num=i), end="")

print()
print("---+----------------------------")

for i in range(1, 10):
    print("{num:>2} | ".format(num=i), end="")
    for j in range(1, 10):
        print("{num:>2} ".format(num=i*j), end="")
    print()
