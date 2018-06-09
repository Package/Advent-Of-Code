from lib import files

PASSPHRASES = files.read_file('input/04.txt')


def valid_passphrase_part_one(passphase: str):
    # Part One
    phrases = passphase.split(' ')
    for p in phrases:
        if phrases.count(p) > 1:
            return False
    return True


def valid_passphrase_part_two(passphrase: str):
    # Part Two
    phrases = passphrase.split(' ')
    for ix, x in enumerate(phrases):
        for iy, y in enumerate(phrases):
            if ix == iy:
                continue
            if is_anagram(x, y):
                return False

    return True


def is_anagram(word_one, word_two):
    """
    Check if the provided words are anagrams, that is you can make the second word using all
    the letters of the first word.
    :param word_one: The first word.
    :param word_two: The second word.
    :return: True if second word is an anagram of the first word, otherwise False.
    """

    # Length of the words do not match so they cannot be anagrams
    if len(word_one) != len(word_two):
        return False

    # Words are already equal, no need to check anything
    if word_one == word_two:
        return True

    # For all the characters in one word, ensure they exist in the second word.
    for c in word_one:
        if c not in word_two:
            return False

        word_two = word_two.replace(c, '', 1)

    return True


print(len([p for p in PASSPHRASES if valid_passphrase_part_one(p)]))
print(len([p for p in PASSPHRASES if valid_passphrase_part_two(p)]))
