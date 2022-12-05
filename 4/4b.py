from parse import parse


# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
#
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:
#
# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.

def validate(input):
    set1 = set(range(input['p1s'], input['p1e']+1))
    set2 = set(range(input['p2s'], input['p2e']+1))
    return len(set1.intersection(set2)) != 0


parsing_scheme = string_scheme = "{p1s:d}-{p1e:d},{p2s:d}-{p2e:d}"



def parsing(s):
    return parse(parsing_scheme, s.replace("\n", "")).named


if __name__ == "__main__":
    # with open("sample.txt") as input:
    with open("input.txt") as input:
        parsed = [parsing(line) for line in input]
        results = [validate(line) for line in parsed]
        print("number of intersections", sum(results))
