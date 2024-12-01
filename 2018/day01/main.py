if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    lists = [[int(y) for y in x.split("   ")] for x in data.split("\n")]

    print("Part 1:", sum(get_differences(*sort_both(*seperate_lists(lists)))))
    print("Part 2:", sum(get_similarity_score(*count_right_occurences(*seperate_lists(lists)))))