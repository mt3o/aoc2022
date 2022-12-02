if __name__ == "__main__":
    with open("input.txt", "r") as f:
        elves = []
        currentElf = 0
        for level in f.readlines():
            if level == "\n":
                elves.append(currentElf)
                currentElf = 0
                continue
            currentElf += int(level.replace("\n", ""))

    currentMax = 0
    currentMaxI = 0

    numbered = [i for i in enumerate(elves)]

    numbered.sort(reverse=True, key=lambda i: i[1])

    print('sum of top 3 elves is',numbered[0][1]+numbered[1][1]+numbered[2][1])
