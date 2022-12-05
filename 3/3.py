def common_symbol(line):
    half_ = len(line)/2
    half = int(half_)
    comp_a = line[0: half]
    comp_b = line[half: len(line)]
    common = set(comp_a).intersection(set(comp_b))
    print("Common item is", common)
    return list(common)[0]


# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
priorities = {}
for score in range(0, 26):
    symbol = chr(score + ord('a'))
    priorities[symbol] = score+1

for score in range(0, 26):
    symbol = chr(score + ord('A'))
    priorities[symbol] = score+27

if __name__ == "__main__":
    # with open("sample.txt") as input:
    with open("input.txt") as input:
        symbols = [common_symbol(line.strip()) for line in input]
        total = sum([priorities[symbol] for symbol in symbols])
        print("Total sum of priorities for common symbols is",total)
