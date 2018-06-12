from lib import files


class Program(object):

    def __init__(self, name, sub_programs, weight):
        self.name = name
        self.sub_programs = sub_programs
        self.weight = int(weight)

    def total_weight(self):
        return self.weight + sum([p.weight for p in programs if p.name in self.sub_programs])

    def __repr__(self):
        return '<Program name={}, weight={}, total_weight={} />'.format(self.name, self.weight, self.total_weight())


def parse_input():
    """
    Parses the input file into a list of Program objects
    :return: A list of programs.
    """
    lines = files.read_file('input/07.txt')
    program_list = []

    for l in lines:
        name = l[:l.index('(')].strip()
        weight = l[l.index('(') + 1:l.index(')')]
        sub_programs = []

        try:
            sub_programs = l[l.index('>') + 1:].strip().split(', ')
        except ValueError:
            pass
        finally:
            program_list.append(Program(name=name, sub_programs=sub_programs, weight=weight))

    return program_list


def is_held_by_program(key):
    """
    Check if the provided key (a program) is being held by another program.
    :param key: The key (program) to check.
    :return: True if the key (program) is held by another program, otherwise False.
    """
    for p in programs:
        if key in p.sub_programs:
            return True
    return False


def solve_part_one():
    # Part One
    for p in programs:
        if len(p.sub_programs) == 0:
            continue
        if not is_held_by_program(p.name):
            return p.name
    return None


def solve_part_two():
    # Todo: ...
    pass


programs = parse_input()
for p in programs:
    print(p)

print(solve_part_one())
