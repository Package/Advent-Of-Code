# https://adventofcode.com/2017/day/12
from lib.files import read_file

programs = {}
communication = {}


def parse_input():
    """
    Parse the input file into a dictionary in the format:
    { program_id: [sub_program_ids] }
    :return:
    """
    d = read_file('input/12.txt')
    for entry in d:
        program_id = int(entry[0:entry.index('<')])
        sub_programs = [int(x) for x in entry[entry.index('>') + 1:].split(',')]
        programs[program_id] = sub_programs
        communication[program_id] = set()


def add_communication(px, py):
    """
    Recursively add the communication links between two programs. This is so we can then count the number of
    unique communcaton streams after to get the answer to part two.
    :param px:
    :param py:
    :return:
    """
    communication[px].add(px)
    communication[px].add(py)
    communication[px].update(programs[py])

    if px == py:
        return

    for y in programs[py]:
        if y in communication[px]:
            communication[px].update(communication[y])
            continue
        add_communication(px, y)


def solve_part_one(key):
    # Part One
    included_programs = set()

    for x in range(10):
        for k, v in programs.items():
            # Program ID is the key being considered
            if k == key:
                included_programs.add(k)

            # Directly connected
            if key in v:
                included_programs.add(k)

            # Any of this programs subprograms already included? If so then we are connected
            # to the key too.
            if any(x in included_programs for x in v):
                included_programs.add(k)
                included_programs.update(v)

    return len(included_programs)


def solve_part_two():
    # Part Two
    for x in range(100):
        for k, v in programs.items():
            for sp in list(v):
                add_communication(k, sp)

    # There's likely a more pythonic way to do this part but I was tired and had enough of
    # this problem by this point.
    unique_sets = []
    for v in communication.values():
        if v in unique_sets:
            continue
        unique_sets.append(v)

    return len(unique_sets)


parse_input()
print(solve_part_one(0))
print(solve_part_two())
