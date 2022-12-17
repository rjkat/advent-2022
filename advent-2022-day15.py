from tqdm import tqdm
example = False
lines = [
'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
]
if not example:
    with open('day15.txt') as fobj:
        lines = fobj.readlines()
sensors = []
beacons = []
for line in lines:
    lhs, rhs = line.strip().lstrip('Sensor at ').split(': ')
    rhs = rhs.lstrip('closest beacon is at')
    parse_coords = lambda s: [int(t.split('=')[1]) for t in s.split(', ')]
    sensors.append(parse_coords(lhs))
    beacons.append(parse_coords(rhs))

def rule_out_x(sensors, beacons, y, size=None):
    ruled_out = []
    for (s, b) in zip(sensors, beacons):
        dy = abs(s[1] - b[1])
        dx = abs(s[0] - b[0])
        c = abs(y - s[1])
        x_range = (dx + dy) - c
        if x_range < 0:
            continue
        x_min = s[0] - x_range
        x_max = s[0] + x_range
        if size is not None:
            x_min = max(0, x_min)
            x_max = min(size, x_max)
        ruled_out.append([x_min, x_max])

    merged = True
    while merged:
        merged = False
        n = len(ruled_out)
        for i in range(n):
            li, ri = ruled_out[i]
            for j in range(i):
                if i == j:
                    continue
                lj, rj = ruled_out[j]
                if (rj + 1) >= li and (lj - 1) <= ri:
                    ruled_out[i][0] = min(li, lj)
                    ruled_out[i][1] = max(ri, rj)
                    ruled_out.pop(j)
                    merged = True
                    break
            if merged:
                break
    return ruled_out


part_2 = True
if not part_2:
    y = 10 if example else 2000000
    ruled_out = rule_out_x(sensors, beacons, y=y)
    n = 0
    same_row_beacons = set([tuple(b) for b in beacons if b[1] == y])
    for r in ruled_out:
        n += r[1] - r[0] + 1
        for b in same_row_beacons:
            if b[0] >= r[0] and b[0] <= r[1]:
                n -= 1
    print(n)
else:
    size = 20 if example else 4000000
    for y in tqdm(list(range(size))):
        ruled_out = rule_out_x(sensors, beacons, y, size=size)
        if len(ruled_out) > 1:
            found_y = y
            found_x = ruled_out[0][1] + 1
            break
    print(f'{found_x * size + found_y}')

