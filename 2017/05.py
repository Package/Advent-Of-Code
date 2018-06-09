from lib import files


def process_instructions_part_one():
    # Part One
    instructions = [int(x) for x in files.read_file('input/05.txt')]
    instruction_index = instructions[0]
    steps_taken = 1

    while 0 <= instruction_index < len(instructions):
        old_index = instruction_index
        instruction_index += instructions[instruction_index]
        instructions[old_index] += 1
        steps_taken += 1

    return steps_taken


def process_instructions_part_two():
    # Part Two
    instructions = [int(x) for x in files.read_file('input/05.txt')]
    instruction_index = instructions[0]
    steps_taken = 1

    while 0 <= instruction_index < len(instructions):
        old_index = instruction_index
        instruction_index += instructions[instruction_index]
        instructions[old_index] += 1 if instructions[old_index] < 3 else -1
        steps_taken += 1

    return steps_taken


print(process_instructions_part_one())
print(process_instructions_part_two())