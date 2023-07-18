#!/usr/bin/python3
alphabet = ""
for ascii_value in range(ord('a'), ord('z')+1):
    alphabet += chr(ascii_value)

print("{}".format(alphabet), end="")
