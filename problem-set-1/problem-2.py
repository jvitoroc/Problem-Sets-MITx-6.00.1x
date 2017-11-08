"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

-> Number of times bob occurs is: 2
"""

occurs = 0
pos = -1
while True:
    c = s.find('bob', pos+1)
    if(c != -1):
        occurs += 1
        pos = c
    else:
        break
print("Number of times bob occurs is: {}".format(occurs))
