#!/usr/bin/env python3

file = open("student1.txt", "r")

content = file.read()
print(content)

file.close()