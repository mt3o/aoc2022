from parse import parse


def validate(input):
    first_overlaps_second = input['p1s'] <= input['p2s'] and input['p1e'] >= input['p2e']
    second_overlaps_first = input['p2s'] <= input['p1s'] and input['p2e'] >= input['p1e']
    return first_overlaps_second or second_overlaps_first


parsing_scheme = string_scheme = "{p1s:d}-{p1e:d},{p2s:d}-{p2e:d}"


def parsing(s):
    return parse(parsing_scheme, s.replace("\n", "")).named


if __name__ == "__main__":
    # with open("sample.txt") as input:
    with open("input.txt") as input:
        parsed = [parsing(line) for line in input]
        results = [validate(line) for line in parsed]
        print("number of overlaps", sum(results))
