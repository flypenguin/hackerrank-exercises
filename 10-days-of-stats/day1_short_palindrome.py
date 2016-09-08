import time

# still no good.


#r = 'kkkkkkz' # should be 15
#works

#r = 'abbaab'  # should be 4
# works

r = 10000 * 'z' + 'aabbbbbbaa'
# should be 709582664
# no good. and waay to slow.


# start

ord_z = ord('z')
ord_a = ord('a')
alpha_len = ord_z - ord_a + 1

#r = input()
s = map(lambda x: ord(x) - ord_a, list(r))
t = bytearray(s)
slen = len(t)

found = 0

for a in range(0, slen - 3):
    print("a=%s (time: %s)"%(a, time.time()))
    if a == 2: break
    for d in range(a + 3, slen):
        if not t[d] == t[a]:
            continue

        # now. create an array / dict with the information "letter" -> <count>
        # then we have for each letter with M' > 0 occurrences (M'*(M'-1)/2)
        # possibilities for the inner matches. add them up and we have all
        # palindrome-counts for a' and d'.

        counts = [0] * alpha_len
        for letter_num in t[a+1:d]:
            counts[letter_num] += 1

        # now we have the array which holds the information of all our letter
        # occurrences (just how many of letter 'a', 'b', ... 'z' are in that
        # part of the string)

        for letter_count in counts:
            found += int(letter_count * (letter_count - 1) / 2)

    found = found % (10**9 + 7)


print(found)