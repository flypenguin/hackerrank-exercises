from math import pow, sqrt


def stddev(a):
    mean = sum(a) / len(a)
    tmp = 0
    for elem in a:
        tmp += pow(elem - mean, 2)
    tmp /= len(a)
    return sqrt(tmp)


num = input()
arr = input()

#num = '5'
#arr = '10 40 30 50 20'         # should be 14.1

num = int(num)
arr = list(map(int, arr.split()))

print("%.1f" % stddev(arr))