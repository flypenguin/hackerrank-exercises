#!/usr/bin/env python3

# read two lines from stdin
# line 1: a <number> which tells you how many numbers are in line two
# line 2: a space-separated list of <number> integers
# finally print the mean, median and mode of the list
# mode: the smallest number, or the number which comes most often.
# if more than one number come "most often", use again the smallest one.


from collections import defaultdict

# read stdin
num = int(input())
arr = sorted(list(map(int, input().split())))
assert num == len(arr)

# calculate mean
mean = sum(arr) / float(num)

# calculate median
tmp = int(num/2)
if num % 2 == 1:
    median = arr[tmp]
else:
    median = (arr[tmp-1] + arr[tmp]) / 2

# calculate mode
mode = candidate = arr[0]
longest = streak = 1
for index in range(num-1):
    elem = arr[index+1]
    if elem == arr[index]:
        streak += 1
        candidate = elem
    else:
        if longest < streak: 
            mode = candidate
            longest = streak
        streak = 1

# print
print(mean)
print(median)
print(mode)
