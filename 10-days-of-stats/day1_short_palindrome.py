#!/usr/bin/python3

# let's try to not do string comparisons and maybe list indexing
# is faster than string indexing
s = list(map(ord, list(input())))

slen = len(s)
found = 0

# baseline optimization only (don't know if there is more possible)
for a in range(0, slen-3):
    for d in range(a+3, slen):
        if not s[d] == s[a]: 
            continue
        for b in range(a+1, d-1):
            for c in range(b+1, d):
                if s[b] == s[c]:
                    found += 1

print(found % (10**9 + 7))
