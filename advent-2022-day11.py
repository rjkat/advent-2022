import numpy as np
from dataclasses import dataclass
from typing import List, Optional, Any

@dataclass
class Monkey:
    number: int
    items: List[int]
    apply_rule: Any
    divisor: int
    throw_to: Any
    n_inspected: int = 0
    part_1: bool = False

    def inspect(self) -> Optional[int]:
        recipients = []
        items = []
        for item in self.items:
            item = self.apply_rule(item)
            if self.part_1:
                item //= 3
            recipients.append(self.throw_to(item))
            items.append(item)
            self.n_inspected += 1
        self.items = []
        return recipients, items

    @classmethod
    def parse(cls, lexed, offset):
        n = 0
        while (offset + n) < len(lexed):
            toks = lexed[offset + n]
            k = toks[0]
            if k == '':
               n += 1
               break 
            if k.startswith('Monkey'):
                number = int(k.split(' ')[1])
            elif k == 'Starting items':
                items = [int(t) for t in toks[1].split(', ')]
            elif k == 'Operation':
                eqn = toks[1].split(' = ')
                syms = eqn[1].split(' ')
                def apply_rule(x):
                    a = x if syms[0] == 'old' else int(syms[0])
                    b = x if syms[2] == 'old' else int(syms[2])
                    return a + b if syms[1] == '+' else a * b
            elif k == 'Test':
                divisor = int(toks[1].lstrip('divisible by '))
                cond_1 = lexed[offset + n + 1]
                case_1 = True if cond_1[0] == 'If true' else False
                recipient_1 = int(cond_1[1].lstrip('throw to monkey '))
                cond_2 = lexed[offset + n + 2]
                recipient_2 = int(cond_2[1].lstrip('throw to monkey '))
                throw_to = lambda x: recipient_1 if ((x % divisor) == 0) == case_1 else recipient_2

            n += 1

        return n, cls(number=number, items=items, divisor=divisor, apply_rule=apply_rule, throw_to=throw_to)

lexed = []
with open('day11.txt') as fobj:
    for l in fobj.readlines():
        lexed.append(l.lstrip().strip().strip(':').split(': '))

offset = 0
monkeys = dict()
while offset < len(lexed):
    n, monkey = Monkey.parse(lexed, offset)
    monkeys[monkey.number] = monkey
    offset += n
monkeys = [monkeys[i] for i in range(len(monkeys))]

factor = 1
for m in monkeys:
    factor *= m.divisor

rounds = 10000
for i in range(rounds):
    for m in monkeys:
        recipients, items = m.inspect()
        for (r, item) in zip(recipients, items):
            item %= factor
            monkeys[r].items.append(item)

n_inspected = sorted([m.n_inspected for m in monkeys])
monkey_business = n_inspected[-2] * n_inspected[-1]
print(monkey_business)
import pdb
pdb.set_trace()