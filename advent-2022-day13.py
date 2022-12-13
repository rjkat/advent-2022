from functools import cmp_to_key
test_case = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]",
]

def parse_lines(lines):
    i = 0
    pairs = []
    while i < len(lines):
        if i < len(lines) and lines[i].strip() == "":
            i += 1
        if i >= len(lines):
            break
        l = eval(lines[i].strip())
        i += 1
        r = eval(lines[i].strip())
        i += 1
        pairs.append((l, r))
    return pairs

with open('day13.txt') as fobj:
    puzzle_input = fobj.readlines()


def compare_order(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return 1
        elif r < l:
            return -1
        return 0
    if isinstance(l, list) and isinstance(r, list):
        if len(l) == 0 and len(r) == 0:
            return 0
        if len(l) == 0 and len(r) > 0:
            return 1
        if len(r) == 0 and len(l) > 0:
            return -1
        l0 = l[0]
        r0 = r[0]
        x = compare_order(l0, r0)
        if x != 0:
            return x
        return compare_order(l[1:], r[1:])
    if isinstance(l, list) and isinstance(r, int):
        return compare_order(l, [r])
    if isinstance(l, int) and isinstance(r, list):
        return compare_order([l], r)

pairs = parse_lines(puzzle_input)
total = 0
for (i, pair) in enumerate(pairs):
    if compare_order(*pair) == 1:
        total += i + 1
print(total)

dividers = [[[2]], [[6]]]
packets = sorted([x for pair in pairs for x in pair] + dividers, key=cmp_to_key(compare_order), reverse=True)
decode_key = 1
for (i, pkt) in enumerate(packets):
    if pkt in dividers:
        decode_key *= i + 1
print(decode_key)
import pdb
pdb.set_trace()