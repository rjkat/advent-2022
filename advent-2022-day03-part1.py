with open('day03.txt', 'rt') as fobj:
    lines = fobj.readlines()

score = 0
for l in lines:
    s = l.strip()
    lhs = set(s[:(len(s)//2)])
    rhs = set(s[(len(s)//2):])
    common = list(lhs.intersection(rhs))
    if common.isupper():
        inc = ord(common) - ord('A') + 27
    else:
        inc = ord(common) - ord('a') + 1
    print(inc)
    score += inc

import pdb
pdb.set_trace()