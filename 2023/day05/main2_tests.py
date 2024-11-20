from main2 import combine_two_ranges

# Same range
assert combine_two_ranges((0, 10, -7), (0, 10, 6)) == ([(0, 10, -1)], [], []), \
    f"{combine_two_ranges((0, 10, -7), (0, 10, 6))} != ([(0, 10, -1)], [], [])"
assert combine_two_ranges((4, 10, 3), (4, 10, 6)) == ([(4, 10, 9)], [], []), \
    f"{combine_two_ranges((4, 10, 3), (4, 10, 6))} != ((4, 10, 9), [], [])"

# Same start different end
assert combine_two_ranges((4, 2, -7), (4, 10, 6)) == ([(4, 2, -1)], [], [(6, 8, 6)]), \
    f"{combine_two_ranges((4, 2, -7), (4, 10, 6))} != ([(4, 2, -1)], [], [(6, 8, 6)])"
assert combine_two_ranges((2, 10, 3), (2, 3, 6)) == ([(2, 3, 9)], [(5, 7, 3)], []), \
    f"{combine_two_ranges((2, 10, 3), (2, 3, 6))} != ([(2, 3, 9)], [(5, 7, 3)], [])"

# Not overlapping
assert combine_two_ranges((3, 2, -7), (6, 2, 6)) == ([(3, 2, -7)], [], [(6, 2, 6)]), \
    f"{combine_two_ranges((3, 2, -7), (6, 2, 6))} != ([(3, 2, -7)], [], [(6, 2, 6)])"
assert combine_two_ranges((7, 3, 3), (2, 3, 6)) == ([], [(7, 3, 3)], []), \
    f"{combine_two_ranges((7, 3, 3), (2, 3, 6))} != ([], [(7, 3, 3)], [])"

# Same end different start
assert combine_two_ranges((4, 3, -7), (5, 2, 6)) == ([(4, 1, -7), (5, 2, -1)], [], []), \
    f"{combine_two_ranges((4, 3, -7), (5, 2, 6))} != ([(4, 1, -7), (5, 2, -1)], [], [])"
assert combine_two_ranges((7, 3, 3), (2, 8, 6)) == ([(7, 3, 9)], [], []), \
    f"{combine_two_ranges((7, 3, 3), (2, 8, 6))} != ([(7, 3, 9)], [], [])"

# From running main
assert combine_two_ranges((57, 13, 0), (53, 8, -4)) == ([(57, 4, -4)], [(61, 9 ,0)], []), \
    f"{combine_two_ranges((57, 13, 0), (53, 8, -4))} != ([(57, 4, -4)], [(61, 9 ,0)], [])"