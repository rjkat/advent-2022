with open('test.txt') as fobj:
    lines = fobj.readlines()
x = []
n = 0
for (i, line) in enumerate(lines):
    l = line.strip()
    if not l:
        x.append(n)
        n = 0
    else:
        n += int(l)

    if len(x) == 66:
        print(f'split at {i}')
x.append(n)
totals = sorted(x, reverse=True)
import pdb
pdb.set_trace()
[print(f'Sum of top {k}: {sum(totals[:k])}') for k in (1, 3)]
