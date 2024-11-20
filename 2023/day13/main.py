def get_col(pattern, index):
    return "".join(x[index] for x in pattern)

def col_matches(pattern, center: int, offset: int):
    return get_col(pattern, center - offset) == get_col(pattern, center + 1 + offset)

def row_matches(pattern, center: int, offset: int):
    return pattern[center - offset] == pattern[center + 1 + offset]

def col_matches_smudge(pattern, center: int, offset: int):
    col1 = get_col(pattern, center - offset)
    col2 = get_col(pattern, center + 1 + offset)
    return sum([a == b for a, b in zip(col1, col2)]) == len(col1) - 1

def row_matches_smudge(pattern, center: int, offset: int):
    col1 = pattern[center - offset]
    col2 = pattern[center + 1 + offset]
    return sum([a == b for a, b in zip(col1, col2)]) == len(col1) - 1

def num_mirror_col_smudges(pattern, col):
    res = 0
    num_iter = min(col, len(pattern[0]) - col - 2) + 1
    for offset in range(num_iter):
        if not col_matches(pattern, col, offset):
            if col_matches_smudge(pattern, col, offset):
                res += 1
            else:
                return -1
    return res

def num_mirror_row_smudges(pattern, row):
    res = 0
    num_iter = min(row, len(pattern) - row - 2) + 1
    for offset in range(num_iter):
        if not row_matches(pattern, row, offset):
            if row_matches_smudge(pattern, row, offset):
                res += 1
            else:
                return -1
    return res

def get_mirror_col(pattern, smudges = 0):
    for col in range(len(pattern[0]) - 1):
        if num_mirror_col_smudges(pattern, col) == smudges:
            return col
    return -1

def get_mirror_row(pattern, smudges = 0):
    for row in range(len(pattern) - 1):
        if num_mirror_row_smudges(pattern, row) == smudges:
            return row
    return -1

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data: str = open(os.path.join(__location__, "input.txt"), "r").read()
    patterns = tuple(tuple(x.split("\n")) for x in data.split("\n\n"))

    print("Part1:", sum([get_mirror_col(pattern) + 1 + (get_mirror_row(pattern) + 1) * 100 for pattern in patterns]))
    print("Part2:", sum([get_mirror_col(pattern, 1) + 1 + (get_mirror_row(pattern, 1) + 1) * 100 for pattern in patterns]))