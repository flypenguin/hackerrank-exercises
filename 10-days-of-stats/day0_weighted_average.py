#!/usr/bin/env python3

# weighted mean
# just another variation on list bending :)
# for REALLY BIG lists this does not scale.
# but we don't have those.


# read input data
num = int(input())
xs = list(map(int, input().split()))
ws = list(map(int, input().split()))
assert num == len(ws) == len(xs)

# calculate weighted mean
numerator = sum([x*y for x, y in zip(xs, ws)])
denominator = sum(ws)
weighted_mean = numerator / float(denominator)

# print result
print("{:.1f}".format(weighted_mean))
