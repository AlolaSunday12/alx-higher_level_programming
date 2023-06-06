#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        for second_ones_digit in range(ones_digit + 1, 10):
            print("{:02d}, {:02d}, {:02d}".format(tens_digit,
                ones_digit, second_ones_digit))
