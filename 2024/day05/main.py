from collections import defaultdict

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    rules, updates = list(data.split("\n\n"))

    rules_dictionary = defaultdict(lambda: set())

    for rule in rules.split("\n"):
        before, after = rule.split("|")
        rules_dictionary[int(before)].add(int(after))

    update_lists = [[int(y) for y in x.split(",")] for x in updates.split("\n")]

    part1 = 0
    part2 = 0

    for update in update_lists:
        changed = False
        checked = set()
        fixed_update = list()

        for page_number in update:
            misplaced_pages = rules_dictionary[page_number].intersection(checked)

            if len(misplaced_pages):
                changed = True
                insertion_index = min([fixed_update.index(misplaced_page) for misplaced_page in misplaced_pages])
                fixed_update.insert(insertion_index, page_number)
            else:
                fixed_update.append(page_number)
            
            checked.add(page_number)

        middle_index = int((len(fixed_update) - 1) / 2)

        if changed:
            part2 += fixed_update[middle_index]
        else:
            part1 += fixed_update[middle_index]

    print("Part 1:", part1)
    print("Part 2:", part2)