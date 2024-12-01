from collections import defaultdict

def seperate_lists(lists):
    left = list()
    right = list()

    for i in range(len(lists)):
        left_value, right_value = lists[i]
        left.append(left_value)
        right.append(right_value)

    return left, right

def sort_both(left, right):
    return sorted(left), sorted(right)

def get_differences(left, right):
    res = []

    for i in range(len(left)):
        res.append(abs(left[i] - right[i]))

    return res

def count_right_occurences(left, right):
    res = defaultdict(lambda: 0)

    for number in right:
        res[number] += 1

    return left, res

def get_similarity_score(left, right_occurences):
    res = list()

    for number in left:
        res.append(number * right_occurences[number])

    return res

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    lists = [[int(y) for y in x.split("   ")] for x in data.split("\n")]

    print("Part 1:", sum(get_differences(*sort_both(*seperate_lists(lists)))))
    print("Part 2:", sum(get_similarity_score(*count_right_occurences(*seperate_lists(lists)))))