import numpy as np
x = [1]
with open('day10.txt') as fobj:
    for line in fobj.readlines():
        toks = line.strip().split()
        x.append(0)
        if toks[0] == 'addx':
            x.append(int(toks[1]))
x = np.cumsum(x)[:-1]
total = 0
for n in (20, 60, 100, 140, 180, 220):
    total += x[n - 1] * n

width = 40
crt = np.arange(len(x)) % width
print('\n'.join([
    ''.join(['#' if p else '.' for p in line])
    for line in (abs(crt - x) <= 1).reshape(-1, width)
]))
