num = int(input())
arr = sorted(list(map(int, input().split())))
assert len(arr) == num

def leftright(l):
    llen = len(l)
    return l[:(llen//2)], l[-(llen//2):]

def median(l):
    llen = len(l)
    if llen % 2 == 1:
        return l[llen//2]
    else:
        return (l[(llen//2)-1]+l[llen//2]) // 2

left, right = leftright(arr)
print(median(left))
print(median(arr))
print(median(right))
