"""
>>> first_pos_after_starting_mark(4,"mjqjpqmgbljsphdztnvjfqwrcgsmlb")
7

>>> first_pos_after_starting_mark(4,"bvwbjplbgvbhsrlpgdmjqwftvncz")
5

>>> first_pos_after_starting_mark(4,"nppdvjthqldpwncqszvftbrmjlhg")
6

>>> first_pos_after_starting_mark(4,"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
10

>>> first_pos_after_starting_mark(4,"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
11

>>> first_pos_after_starting_mark(14,"mjqjpqmgbljsphdztnvjfqwrcgsmlb")
19
>>> first_pos_after_starting_mark(14,"bvwbjplbgvbhsrlpgdmjqwftvncz")
23
>>> first_pos_after_starting_mark(14,"nppdvjthqldpwncqszvftbrmjlhg")
23
>>> first_pos_after_starting_mark(14,"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
29
>>> first_pos_after_starting_mark(14,"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
26

"""

#run test with python -m doctest -v 6.py



def first_pos_after_starting_mark(unique_chars_to_start_signal, data):

    last_candidate_offset = len(data) - unique_chars_to_start_signal

    for start_offset in range(0, last_candidate_offset):
        end_offset = start_offset + unique_chars_to_start_signal
        to_check = data[start_offset:end_offset]
        if len(set(to_check)) == len(to_check):
            return end_offset


# for running tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readline().strip()
    print("First task:",first_pos_after_starting_mark(4, data))
    print("Second task:",first_pos_after_starting_mark(14, data))
