def is_increasing(a, b):
    return a - b < 0

def changed(a, b):
    return a != b

def safe(a, b, should_increase):
    return changed(a, b) and is_increasing(a, b) is should_increase and abs(a - b) <= 3

def safe_dampend(report, index):
    dampend_report = dampen_report(report, index)

    return all([safe(dampend_report[i], dampend_report[i + 1], is_increasing(dampend_report[0], dampend_report[1])) for i in range(0, len(dampend_report) - 1)])

def dampen_report(report, index):
    return report[:index] + report[index + 1:]

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    reports = [[int(y) for y in x.split(" ")] for x in data.split("\n")]

    print("Part 1:", len([report for report in reports if all([safe(report[i], report[i + 1], is_increasing(report[0], report[1])) for i in range(0, len(report) - 1)])]))
    print("Part 2:", len([report for report in reports if any([safe_dampend(report, index) for index in range(len(report))])]))