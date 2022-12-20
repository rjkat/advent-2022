import numpy as np
ROCK_CHARS = [
    ['####'],
    [
        '.#.',
        '###',
        '.#.',
    ],
    [
        '..#',
        '..#',
        '###'
    ],
    [
        '#',
        '#',
        '#',
        '#'
    ],
    [
        '##',
        '##'
    ]
]

ROCKS = [np.array([[c == '#' for c in row] for row in rock]) for rock in ROCK_CHARS]
# INPUT = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
with open('day17.txt', 'rt') as fobj:
    INPUT = fobj.read().strip()
CHAMBER_WIDTH = 7
MAX_ROCK_HEIGHT = max([len(r) for r in ROCK_CHARS])
DROP_DISTANCE_TO_LEFT_WALL = 2
DROP_HEIGHT_ABOVE_GROUND = 3
INITIAL_HEIGHT = DROP_HEIGHT_ABOVE_GROUND + 2 * MAX_ROCK_HEIGHT + 1
chamber = np.zeros((INITIAL_HEIGHT, CHAMBER_WIDTH), dtype=np.bool8)
chamber[-1, :] = 1

def highest_rock(chamber):
    if not np.any(chamber):
        return chamber.shape[0]
    return np.min(np.nonzero(chamber)[0])

def drop_rock(chamber, rock, input_sequence, input_offset=0):
    height, width = rock.shape
    drop_x = DROP_DISTANCE_TO_LEFT_WALL
    drop_y = highest_rock(chamber) - DROP_HEIGHT_ABOVE_GROUND
    if drop_y < height:
        chamber = np.vstack((np.zeros((height, CHAMBER_WIDTH), dtype=np.bool8), chamber))
        drop_y = highest_rock(chamber) - DROP_HEIGHT_ABOVE_GROUND
    
    i = input_offset
    x, y = drop_x, drop_y
    done = False
    while True:
        if y >= chamber.shape[0]:
            break
        move = input_sequence[i]
        i += 1
        i %= len(input_sequence)
        x_inc = 1 if move == '>' else -1
        next_x = x + x_inc
        next_x = min(max(next_x, 0), CHAMBER_WIDTH - width)
        space = chamber[(y - height):y, next_x:(next_x + width)]
        if not np.any(np.logical_and(space, rock)):
            x = next_x
        y += 1
        space = chamber[(y - height):y, x:(x + width)]
        if np.any(np.logical_and(space, rock)):
            break

    y -= 1
    chamber[(y - height):y, x:(x + width)] |= rock


    return chamber, i

def print_chamber(chamber):
    for (i, row) in enumerate(chamber):
        if i == chamber.shape[0] - 1:
            print('+' + ('-' * CHAMBER_WIDTH) + '+')
        else:
            print('|' + ''.join(['#' if c else '.' for c in row]) + '|')

num_rocks = 0
input_offset = 0

seen = dict()
heights = dict()
cycle_length = None
SIMULATION_LEN = 1000000000000
ncycle = 0
while num_rocks < SIMULATION_LEN and ncycle < 2:
    rock_kind = num_rocks % len(ROCKS)
    chamber, input_offset = drop_rock(chamber, ROCKS[rock_kind], INPUT, input_offset=input_offset)
    top_row = highest_rock(chamber)
    combination = chamber[top_row:(top_row + MAX_ROCK_HEIGHT)]
    if len(combination) == MAX_ROCK_HEIGHT and np.all(np.max(combination, axis=0)):
        x = np.packbits(combination).view('uint32')[0]
        state = (x, rock_kind, input_offset)
        if cycle_length is None:
            if state in seen:
                cycle_start = seen[state]
                cycle_length = num_rocks - cycle_start
            else:
                seen[state] = num_rocks
    
    heights[num_rocks] = chamber.shape[0] - highest_rock(chamber) - 1
    if cycle_length is not None:
        ncycle = (num_rocks - cycle_start) // cycle_length
    num_rocks += 1


num_rocks = cycle_start + 1
total_height = heights[cycle_start]
cycle_height = heights[cycle_start + cycle_length] - heights[cycle_start]

ncycle = (SIMULATION_LEN - cycle_start) // cycle_length

total_height += ncycle * cycle_height
num_rocks += ncycle * cycle_length

remaining = SIMULATION_LEN - num_rocks
total_height += heights[cycle_start + remaining] - heights[cycle_start]
print(total_height)
import pdb
pdb.set_trace()




