INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\09\input.txt"
TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".split('\n')


def get_input(test=False):
    if test:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


def sanitize_input(input_list: list[str]):
    if not input_list[-1]:
        del input_list[-1]
    input_list = [(char, int(num))
                  for char, num in map(lambda i: i.split(" "), input_list)]
    return input_list


def part1(input_list: list[tuple[str, int]]):
    tx, ty, hx, hy = 0, 0, 0, 0
    visited = set()
    dir_map = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    def move_head(dx, dy):
        nonlocal hx, hy
        hx += dx
        hy += dy

    def move_tail():
        nonlocal tx, ty
        dx, dy = hx - tx, hy - ty
        absdx, absdy = abs(dx), abs(dy)
        if absdx > (0 if absdy > 1 else 1):
            tx += dx // absdx
        if absdy > (0 if absdx > 1 else 1):
            ty += dy // absdy

    for char, num in input_list:
        for _ in range(num):
            move_head(*dir_map[char])
            move_tail()
            visited.add((tx, ty))
    answer = len(visited)
    return answer


def part2(input_list: list[tuple[str, int]]):
    visited = set()
    dir_map = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    knots = [[0, 0] for _ in range(10)]

    def move_head(head_list, dx, dy):
        head_list[0] += dx
        head_list[1] += dy

    def move_tail(this_knot, prev_knot):
        (hx, hy), (tx, ty) = prev_knot, this_knot
        dx, dy = hx - tx, hy - ty
        absdx, absdy = abs(dx), abs(dy)
        if absdx > (0 if absdy > 1 else 1):
            this_knot[0] += dx // absdx
        if absdy > (0 if absdx > 1 else 1):
            this_knot[1] += dy // absdy

    for char, num in input_list:
        for _ in range(num):
            move_head(knots[0], *dir_map[char])
            for this_knot, prev_knot in zip(knots[1:], knots):
                move_tail(this_knot, prev_knot)
            visited.add(tuple(knots[-1]))
    answer = len(visited)
    return answer


def main():
    input_list = get_input(test=1)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
