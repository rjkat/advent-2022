import numpy as np
lines = [
    'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB',
    'Valve BB has flow rate=13; tunnels lead to valves CC, AA',
    'Valve CC has flow rate=2; tunnels lead to valves DD, BB',
    'Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE',
    'Valve EE has flow rate=3; tunnels lead to valves FF, DD',
    'Valve FF has flow rate=0; tunnels lead to valves EE, GG',
    'Valve GG has flow rate=0; tunnels lead to valves FF, HH',
    'Valve HH has flow rate=22; tunnel leads to valve GG',
    'Valve II has flow rate=0; tunnels lead to valves AA, JJ',
    'Valve JJ has flow rate=21; tunnel leads to valve II'
]

# with open('day16.txt') as fobj:
#     lines = fobj.readlines()

connected = dict()
flow = dict()
for line in lines:
    toks = line.strip().split(' ')
    i = 0
    valve = toks[1]
    flow[valve] = int(toks[4].split('=')[1].strip(';'))
    connected[valve] = [t.strip(',') for t in toks[9:]]

valves = sorted(list(flow.keys()))
best_moves = dict()
MAX_STEPS = 30



def score_state(valve, t, valves_open):
    if t > MAX_STEPS:
        return 0
    pressure = 0
    for v in valves_open:
        pressure += flow[v]
    if t == MAX_STEPS:
        return pressure

    if (valve, t, valves_open) in best_moves:
        return best_moves[(valve, t, valves_open)][0]

    best_move_score = None
    best_move = None
    for other in connected[valve]:
        move_score = score_state(other, t + 1, valves_open) + pressure
        if best_move is None or move_score > best_move_score:
            best_move_score = move_score
            best_move = other
    best_score = best_move_score
    next_valves_open = valves_open

    if valve not in valves_open and flow[valve] > 0:
        best_open_move_score = None
        best_open_move = None
        possible_open = tuple(sorted(list(valves_open) + [valve]))
        for other in connected[valve]:
            open_score = score_state(other, t + 2, possible_open) + 2*pressure + flow[valve]
            if best_open_move_score is None or open_score > best_open_move_score:
                best_open_move_score = open_score
                best_open_move = other
        if best_open_move_score > best_move_score:
            best_move = valve
            best_score = best_open_move_score
            next_valves_open = possible_open
            best_moves[(valve, t + 1, next_valves_open)] = (best_score - pressure, best_open_move, t + 2, possible_open)

    best_moves[(valve, t, valves_open)] = (best_score, best_move, t + 1, next_valves_open)
    return best_score


start_location = 'AA'
start_valves_open = ()
most_pressure = score_state(start_location, 1, start_valves_open)

i = 0
total = 0
moves = []
t = 0

move = (most_pressure, start_location, 1, start_valves_open)
moves = []
while move is not None:
    moves.append(move)
    score, location, t, valves_open = move
    move = best_moves.get((location, t, valves_open), None)
print(most_pressure)

import pdb
pdb.set_trace()