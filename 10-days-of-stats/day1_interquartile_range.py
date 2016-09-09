def leftright(l):
    llen = len(l)
    return l[:(llen//2)], l[-(llen//2):]


def median(l):
    llen = len(l)
    if llen % 2 == 1:
        return l[llen//2]
    else:
        return (l[(llen//2)-1]+l[llen//2]) / 2


# really the hardest part is to *understand* what this task is actually about.
# funnily, then it is really pretty much super easy.


# for testing
i1 = '6'
i2 = '6 12 8 10 20 16'
i3 = '5 4 3 2 1 5'

i1 = input()
i2 = input()
i3 = input()

i1 = i1
i2 = list(map(int, i2.split()))
i3 = list(map(int, i3.split()))

final_arr = []
for elem, freq in zip(i2, i3):
    final_arr += [elem] * freq
final_arr.sort()

l, r = leftright(final_arr)
iqt = median(r) - median(l)
print("%.1f" % iqt)
