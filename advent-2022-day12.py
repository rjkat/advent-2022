import numpy as np
import functools

test_case = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi"
]
with open('day12.txt') as fobj:
    puzzle_input = fobj.readlines()

def parse_elevations(lines):
    start, end = (None, None)
    el = []
    for (i, line) in enumerate(lines):
        line = line.strip()
        if 'S' in line:
            start = (i, line.find('S'))
            line = line.replace('S', 'a')
        if 'E' in line:
            end = (i, line.find('E'))
            line = line.replace('E', 'z')
        el.append([ord(c) - ord('a') for c in line])
    return start, end, np.array(el)

def fewest_steps(start, end, elevations):
    max_steps = np.prod(elevations.shape)
    steps = np.zeros_like(elevations) + max_steps
    height, width = elevations.shape
    done = False
    n = 1
    to_try = [(end, n)]
    while len(to_try) > 0:
        pos, n = to_try.pop(0)
        if pos[0] == start[0] and pos[1] == start[1]:
            break
        row, col = pos
        el = elevations[row, col]
        moves = []
        if (row + 1) < height:
            moves.append((row + 1, col))
        if (row - 1) >= 0:
            moves.append((row - 1, col))
        if (col + 1) < width:
            moves.append((row, col + 1))
        if (col - 1) >= 0:
            moves.append((row, col - 1))
        moves = [m for m in moves if (el - elevations[m]) <= 1]
        for m in moves:
            if steps[m] == max_steps and m != end:
                steps[m] = n
                to_try.append((m, n + 1))
    return steps


s, e, el = parse_elevations(puzzle_input)

steps = fewest_steps(s, e, el)
print(f'part 1: {steps[s]}')
possible_starts = [tuple(s) for s in np.argwhere(el == 0)]

fewest =  np.prod(el.shape)
best_steps = None
for s in possible_starts:
    steps = fewest_steps(s, e, el)
    if steps[s] < fewest:
        fewest = steps[s]
        best_steps = steps
print(f'part 2: {fewest}')
import pdb
pdb.set_trace()
