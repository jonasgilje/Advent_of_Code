INPUT_FILE = "14\\input.txt"
TEST = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".split("\n")


def get_input(test=False):
    if test:
        return TEST

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)

    return input_list


def sanitize_input(input_list):
    if not input_list[-1]:
        del input_list[-1]

    grid: set[tuple[int, int]] = set()

    def split_line(line: str):
        return [tuple(map(int, p.split(","))) for p in line.split(" -> ")]

    def points_between(p1: tuple[int, int], p2: tuple[int, int]):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            return {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}
        elif y1 == y2:
            return {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}
        raise ValueError

    for l in input_list:
        l_split = split_line(l)
        for p1, p2 in zip(l_split, l_split[1:]):
            grid |= points_between(p1, p2)

    return grid


def part1(grid: set[tuple[int, int]]):
    grid = grid.copy()
    max_y = max(y for _, y in grid)

    def add_sand(x, y):
        if y > max_y:
            return False
        down = (x, y+1)
        down_left = (x-1, y+1)
        down_right = (x+1, y+1)
        if down in grid:
            if down_left not in grid:
                return add_sand(*down_left)
            if down_right not in grid:
                return add_sand(*down_right)
            grid.add((x, y))
            return True
        return add_sand(*down)

    answer = 0
    while add_sand(500, 0):
        answer += 1

    return answer


def part2(grid: set[tuple[int, int]]):
    grid = grid.copy()
    max_y = max(y for _, y in grid)

    def count_sand(x, y):
        if (x, y) in grid or y > max_y + 1:
            return 0
        grid.add((x, y))

        return 1 + count_sand(x-1, y+1) + count_sand(x, y+1) + count_sand(x+1, y+1)

    answer = count_sand(500, 0)
    return answer


def main():
    input_list = get_input(test=0)
    grid = sanitize_input(input_list)
    ans1 = part1(grid)
    ans2 = part2(grid)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
