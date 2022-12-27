import re
import collections


INPUT_FILE = "15\\input.txt"
TEST = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".split("\n")


def get_input(test=False):
    if test:
        return TEST

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)

    return input_list


def sanitize_input(input_list: list[str]) -> list[tuple[int, int, int, int]]:
    if not input_list[-1]:
        del input_list[-1]

    return [tuple(int(d) for d in re.findall("-?\d+", l)) for l in input_list]


def manhattan_distance(x1: int, y1: int, x2: int, y2: int):
    return abs(x1 - x2) + abs(y1 - y2)


def part1(input_list: list[tuple[int, int, int, int]]):
    # result_y = 10
    result_y = 2_000_000

    def points_in_row(row_y: int, x: int, y: int, man_dist: int):
        perp = man_dist - abs(y - row_y)
        result: set[tuple[int, int]] = set()
        for i in range(perp + 1):
            result |= {(x - i, row_y), (x + i, row_y)}
        return result

    man_dists = [manhattan_distance(*l) for l in input_list]
    beacons_in_row = {t[2:] for t in input_list if t[3] == result_y}
    result: set[tuple[int, int]] = set()
    for t, d in zip(input_list, man_dists):
        result |= points_in_row(result_y, *t[:2], d)

    result -= beacons_in_row

    return len(result)


def part2(input_list: list[tuple[int, int, int, int]]):
    # Might be a dubious solution. Attempts to find candidate Beacon Exclusion
    # Zones where the gap between two sensors allows for a distress signal to
    # be placed between them. Then chooses the intersection points between the
    # candidate list of points.
    man_dists = [manhattan_distance(*l) for l in input_list]

    interesting_list = []

    for i in range(len(input_list)):
        for j in range(i):
            a = manhattan_distance(*input_list[i][:2], *input_list[j][:2])
            b = man_dists[i] + man_dists[j]
            if a == b + 2:
                interesting_list.append((i, j))

    def bez_between(i: int, j: int):
        result_set: set[tuple[int, int]] = set()
        if man_dists[i] > man_dists[j]:  # => i has lowest man_dist
            i, j = j, i
        x1, y1, *_, man_dist1 = *input_list[i], man_dists[i]
        x2, y2, *_ = input_list[j]
        sign_dx = (x2 - x1) // abs(x2 - x1)
        sign_dy = (y2 - y1) // abs(y2 - y1)
        for i in range(man_dist1 + 2):
            px = x1 + i*sign_dx
            py = y1 + (man_dist1 + 1 - i)*sign_dy
            result_set.add((px, py))
        return result_set

    points_dict: collections.defaultdict[tuple[int,
                                               int], int] = collections.defaultdict(int)
    for ps in interesting_list:
        for candidate_point in bez_between(*ps):
            points_dict[candidate_point] += 1

    answer_x, answer_y = max(points_dict, key=points_dict.get)
    answer = answer_x * 4_000_000 + answer_y
    return answer


def main():
    input_list = get_input(test=0)
    grid = sanitize_input(input_list)
    ans1 = part1(grid)
    ans2 = part2(grid)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
