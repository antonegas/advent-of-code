from functools import reduce

def update_bounds(bounds, update_key, lower = 1, upper = 4000):
    return {k: (max(lower, bounds[k][0]), min(upper, bounds[k][1])) if k == update_key else (bounds[k][0], bounds[k][1]) for k in bounds}

def next_from_workflow(work_flow, ratings):
    for rule in work_flow[:-1]:
        next_key = next_from_rule(rule, ratings)
        if next_key != "":
            return next_key
    return work_flow[-1]

def next_from_rule(rule, ratings):
    condition, next_key = rule.split(":")
    rating = ratings[condition[0]]
    condition_operand = condition[1]
    value = int(condition[2:])

    if condition_operand == ">" and rating > value:
        return next_key
    elif condition_operand == "<" and rating < value:
        return next_key
    else:
        return ""

def accepted(work_flows, ratings):
    current_workflow = "in"
    
    while True:
        if current_workflow == "A":
            return True
        elif current_workflow == "R":
            return False
        else:
            current_workflow = next_from_workflow(work_flows[current_workflow], ratings)

def total_rating(rating):
    return sum(list(rating.values()))

def possible_values(work_flows, work_flow, index, bounds):
    if work_flow == "A":
        return reduce(lambda a, b: a * b, [max(0, v[1] - v[0] + 1) for v in bounds.values()])
    elif work_flow == "R":
        return 0
    
    current = work_flows[work_flow][index]
    
    if ":" not in current:
        return possible_values(work_flows, current, 0, bounds)
    
    rule, next_key = current.split(":")
    key = rule[0]
    condition = rule[1]
    value = int(rule[2:])

    if condition == ">":
        return possible_values(work_flows, next_key, 0, update_bounds(bounds, key, lower=value + 1)) + possible_values(work_flows, work_flow, index + 1, update_bounds(bounds, key, upper=value))
    else: # <
        return possible_values(work_flows, next_key, 0, update_bounds(bounds, key, upper=value - 1)) + possible_values(work_flows, work_flow, index + 1, update_bounds(bounds, key, lower=value))

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    work_flows, all_ratings = data.split("\n\n")

    work_flows = {k: list(v[:-1].split(",")) for k, v in list(x.split("{") for x in work_flows.split("\n"))}
    all_ratings = list({k: int(v) for k, v in list(list(z.split("=")) for z in y)} for y in list(x[1:-1].split(",") for x in all_ratings.split("\n")))

    print("Part 1:", sum([total_rating(rating) for rating in all_ratings if accepted(work_flows, rating)]))
    print("Part 2:", possible_values(work_flows, "in", 0, {k: (1, 4000) for k in "xmas"}))