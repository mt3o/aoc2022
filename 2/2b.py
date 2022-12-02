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
}

loses_to = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}
wins_with = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors',
}
draw = {
    'scissors': 'scissors',
    'rock': 'rock',
    'paper': 'paper',
}
how_ends = {
    'X': loses_to,
    'Y': draw,
    'Z': wins_with,
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
    opponent, strategy = line.replace("\n", "").split(" ")
    opponent = symbols[opponent]
    me = how_ends[strategy][opponent]
    result = results[me + opponent]
    return scores[result] + scores[me]


if __name__ == "__main__":
    # with open("sample.txt", "r") as f:
    with open("input.txt", "r") as f:
        scores = [evaluate(line) for line in f]
    score = sum(scores)
    print("final score is", score)
