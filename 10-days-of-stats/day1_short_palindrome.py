from collections import defaultdict

# testset: s='kkkkkkz', result=15, with this we get 14.

#s = list(map(ord, list(input())))
#s = "apopohauugha"
s = 'kkkkkkz'
slen = len(s)

found = 0

# there must be cause this timeouts.
countdict = defaultdict(int)
cd_start = 1
a = 0
for d in range(a + 3, slen):
    if not s[d] == s[a]:
        continue
    else:
        for idx in range(cd_start, d):
            countdict[s[idx]] += 1
        cd_start = d
        for val in countdict.values():
            val_tmp = val - 1
            found += int((val_tmp / 2) * (val_tmp + 1))
for a in range(0, slen - 3):
    countdict[s[a]] -= 1
    assert countdict[s[a]] >= 0
    for val in countdict.values():
        found += int((val / 2) * (val + 1))

print(found % (10 ** 9 + 7))