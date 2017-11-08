"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

->Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

->Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""

l = len(s)
res = ''
for i in range(l-2):
    start,end,j = i,i,i
    while j < l-1 and (ord(s[j]) <= ord(s[j+1])):
        end, j = end+1,j+1
    if(len(s[start:end+1]) > len(res)):
        res = s[start:end+1]
print(res)
