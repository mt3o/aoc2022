from collections import deque

from parse import parse

stacks_input = [l.replace("[", "").replace("]", "").replace("   ", "!") for l in """
   [M]         [Z]   [V]   
   [Z]   [P]   [L]   [Z][J]
[S][D]   [W]   [W]   [H][Q]
[P][V][N][D]   [P]   [C][V]
[H][B][J][V][B][M]   [N][P]
[V][F][L][Z][C][S][P][S][G]
[F][J][M][G][R][R][H][R][L]
[G][G][G][N][V][V][T][Q][F]
""".split("\n") if l.strip() != ""]

stacks = [deque() for _ in stacks_input[-1]]
for line_nr, line in enumerate(stacks_input):
    for stack_nr, stack_item in enumerate(line):
        if stack_item != "!":
            stacks[stack_nr].appendleft(stack_item)


def parse_input(line):
    format = "move {amount:d} from {source:d} to {destination:d}"
    return parse(format, line).named


def apply_command(command):
    amount = command['amount']
    source = command['source']
    destination = command['destination']
    stacks[destination - 1].append(stacks[source - 1].pop())
    amount = amount - 1
    if amount > 0:
        return apply_command({
            "source": source,
            "destination": destination,
            "amount": amount
        })


if __name__ == '__main__':
    with open("input.txt") as f:
        data_raw = [line.strip() for line in f if line.startswith("move")]
        data = [parse_input(line) for line in data_raw]
        for command in data:
            apply_command(command)

        print("Top of each stack is:")
        for n,stack in enumerate(stacks):
            print(stack.pop(), end="")
