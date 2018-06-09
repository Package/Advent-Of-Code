# https://adventofcode.com/2017/day/6


def redistribute(b):
    """
    Redistributes the memory block such that, the memory from the the block with the most memory is shared out
    amongst all memory blocks.
    :return: Returns the redistributed blocks
    """
    blocks = [x for x in b]
    big_index, big_block = biggest_block(blocks)
    blocks[big_index] = 0

    redistribution_index = big_index + 1
    while big_block > 0:
        # Wrap back around when we reach the end of the blocks
        if redistribution_index >= len(blocks):
            redistribution_index = 0

        blocks[redistribution_index] += 1
        big_block -= 1
        redistribution_index += 1

    return blocks


def biggest_block(blocks):
    """
    Finds the block of memory with the highest block count. Returns a tuple containing the index of the block,
    and the number of blocks in the memory block.
    :return: Tuple containing index of the biggest block, value of the biggest block.
    """
    big_block = None
    big_index = None
    for ib, b in enumerate(blocks):
        if big_block is None or b > big_block:
            big_index = ib
            big_block = b

    return big_index, big_block


def process_part_one():
    # Part One
    redistribution_cycles = 0
    block_cache = [[14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]]
    while True:
        new_blocks = redistribute(block_cache[-1])
        redistribution_cycles += 1

        if new_blocks in block_cache:
            return redistribution_cycles
        else:
            block_cache.append(new_blocks)


def process_part_two():
    # Part Two
    redistribution_cycles = 0
    block_cache = [[14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]]
    while True:
        new_blocks = redistribute(block_cache[-1])
        redistribution_cycles += 1

        if new_blocks in block_cache:
            return redistribution_cycles - block_cache.index(new_blocks)
        else:
            block_cache.append(new_blocks)


print(process_part_one())
print(process_part_two())


