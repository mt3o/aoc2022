if __name__ == "__main__":
    with open("input.txt", "r") as f:
        elves = []
        currentElf = 0
        for level in f.readlines():
            if level == "\n":
                elves.append(currentElf)
                currentElf = 0
                continue
            currentElf += int(level.replace("\n",""))

    currentMax = 0
    currentMaxI = 0

    for i, elf in enumerate(elves):
        if currentMax < elf:
            currentMax = elf
            currentMaxI = i
    print('elf number',currentMaxI, 'is carrying ',currentMax,'calories and that is the answer')