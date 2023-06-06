#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{0:02d}, {1:02d}".format(tens_digit, ones_digit))
