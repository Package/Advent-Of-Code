
def read_file(filename):
    with open(filename) as f:
        return [x.replace('\n', '') for x in f.readlines()]
