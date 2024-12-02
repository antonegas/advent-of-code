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



    # p1 = 0
    # p2 = 0

    # for i in lev:
    #     t = True
    #     f = True
    #     h = False
        
    #     for b in range(len(i)):
    #         a = i[:b] + i[b+1:]
    #         t = True
    #         h = False
    #         f = True
    #         if a == [1, 2, 4, 5]:
    #             print("hey", b)
    #         for n in range(len(a)- 1):
    #             d = (a[n] - a[n+1])
    #             g = d > 0
    #             if d == 0:
    #                 t = False
    #                 break
    #             if f:
    #                 f = False
    #                 h = g
    #             elif g != h:
    #                 t = False
    #                 break

    #             if (abs(d) > 3):
    #                 t = False
    #                 break
    #         if t:
    #             break

    #     if t:
    #         p1 += 1


    # for i in range(1, len(reports[0]) - 1):
    #     print(safe(reports[0][i], reports[0][i+1], is_increasing(reports[0][0], reports[0][1])))


    print("Part 1:", len([report for report in reports if all([safe(report[i], report[i + 1], is_increasing(report[0], report[1])) for i in range(0, len(report) - 1)])]))
    print("Part 2:", len([report for report in reports if any([safe_dampend(report, index) for index in range(len(report))])]))