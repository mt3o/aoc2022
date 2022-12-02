scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,

    'lost': 0,
    'draw': 3,
    'won': 6
}

symbols = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',

    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

results = {
    'rockrock': 'draw',
    'paperpaper': 'draw',
    'scissorsscissors': 'draw',

    'rockpaper': 'lost',
    'rockscissors': 'won',
    'paperscissors': 'lost',
    'paperrock': 'won',
    'scissorsrock': 'lost',
    'scissorspaper': 'won',
}


def evaluate(line):
    opponent, me = line.replace("\n", "").split(" ")
    me = symbols[me]
    opponent = symbols[opponent]

    result = results[me+opponent]
    return scores[result] + scores[me]


if __name__ == "__main__":
    # with open("sample.txt", "r") as f:
    with open("input.txt", "r") as f:
        scores = [evaluate(line) for line in f]
    score = sum(scores)
    print("final score is", score)