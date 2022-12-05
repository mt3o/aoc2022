import itertools

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
priorities = {}
for score in range(0, 26):
    symbol = chr(score + ord('a'))
    priorities[symbol] = score + 1

for score in range(0, 26):
    symbol = chr(score + ord('A'))
    priorities[symbol] = score + 27


def process_trigroups(tri):
    g0 = set(tri[0])
    g1 = set(tri[1])
    g2 = set(tri[2])
    common = g0 & g1 & g2
    return list(common)[0]


if __name__ == "__main__":
    # with open("sample.txt") as input:
    with open("input.txt") as input:
        lines = [line.strip() for line in input]
        trigroups = [_ for _ in zip(lines[0:], lines[1:], lines[2:])][::3]
        common_items = [process_trigroups(_) for _ in trigroups]
        scores = [priorities[badge] for badge in common_items]
        print("total score is", sum(scores))
