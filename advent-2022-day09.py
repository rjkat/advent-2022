
update = {
    0 + 2j: 0 + 1j,
    1 + 2j: 1 + 1j,
    2 + 1j: 1 + 1j,
    2 + 0j: 1 + 0j,
    2 + 2j: 1 + 1j,
}
for k, v in list(update.items()):
    update[-k] = -v
for k, v in list(update.items()):
    update[1j * k] = 1j * v
mapping = dict(L=-1+0j, R=1+0j, U=0-1j, D=0+1j)
moves = []
with open('day09.txt') as fobj:
    for line in fobj.readlines():
        toks = line.strip().split()
        direction = mapping[toks[0]]
        moves.extend([direction] * int(toks[1]))

n = 10
rope = [0 for i in range(n)]
visited = {rope[-1]}
for move in moves:
    rope[0] += move
    for i in range(n - 1):
        diff = rope[i] - rope[i + 1]
        rope[i + 1] += update.get(diff, 0)
    visited.add(rope[-1])
print(len(visited))
