INPUT_FILE = "12\\input.txt"
TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
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
    return input_list


def part1(input_list: list[str]):
    def can_goto(x: int, y: int):
        curr_heuristic = heuristic(x, y)
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def is_okay(dx: int, dy: int) -> bool:
            if not (0 <= x+dx < len(input_list[0]) and
                    0 <= y+dy < len(input_list)):
                return False
            return heuristic(x+dx, y+dy) >= curr_heuristic - 1
        return ((x+dx, y+dy) for dx, dy in dirs if is_okay(dx, dy))

    def heuristic(x: int, y: int):
        s = input_list[y][x].replace("S", "a").replace("E", "z")
        return ord("z") - ord(s)  # z0, a25

    def insert_into_open_list(point_tuple: tuple[tuple[int, int], int, int]):
        for i, (_, _, f) in enumerate(open_list):
            if f > point_tuple[2]:
                open_list.insert(i, point_tuple)
                return
        open_list.append(point_tuple)

    start_node: tuple[int, int]
    end_node: tuple[int, int]

    for y, l in enumerate(input_list):
        for x, c in enumerate(l):
            if c == "S":
                start_node = x, y
            elif c == "E":
                end_node = x, y

    # node, g, f
    open_list: list[tuple[tuple[int, int], int, int]] = [(start_node, 0, 0)]
    closed_list: set[tuple[int, int]] = set()

    while open_list:
        current_node, current_g, _ = open_list.pop(0)
        closed_list.add(current_node)
        if current_node == end_node:
            break
        for child in can_goto(*current_node):
            if child in closed_list:
                continue
            child_g = current_g + 1

            for point, g, _ in open_list:
                if point == child and child_g >= g:
                    break
            else:
                insert_into_open_list(
                    (child, child_g, child_g + heuristic(*child)))

    answer = current_g
    return answer


def part2(input_list: list[str]):
    def can_goto(x: int, y: int):
        curr_heuristic = heuristic(x, y)
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def is_okay(dx: int, dy: int) -> bool:
            if not (0 <= x+dx < len(input_list[0]) and
                    0 <= y+dy < len(input_list)):
                return False
            return heuristic(x+dx, y+dy) >= curr_heuristic - 1
        return ((x+dx, y+dy) for dx, dy in dirs if is_okay(dx, dy))

    def heuristic(x: int, y: int):
        s = input_list[y][x].replace("S", "a").replace("E", "z")
        return ord("z") - ord(s)  # z0, a25

    def insert_into_open_list(point_tuple: tuple[tuple[int, int], int, int]):
        for i, (_, _, f) in enumerate(open_list):
            if f > point_tuple[2]:
                open_list.insert(i, point_tuple)
                return
        open_list.append(point_tuple)

    end_node: tuple[int, int]

    # node, g, f
    open_list: list[tuple[tuple[int, int], int, int]] = []
    closed_list: set[tuple[int, int]] = set()

    for y, l in enumerate(input_list):
        for x, c in enumerate(l):
            if c in "Sa":
                open_list.append(((x, y), 0, 0))
            elif c == "E":
                end_node = x, y

    while open_list:
        current_node, current_g, _ = open_list.pop(0)
        closed_list.add(current_node)
        if current_node == end_node:
            break
        for child in can_goto(*current_node):
            if child in closed_list:
                continue
            child_g = current_g + 1

            for point, g, _ in open_list:
                if point == child and child_g >= g:
                    break
            else:
                insert_into_open_list(
                    (child, child_g, child_g + heuristic(*child)))

    answer = current_g
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
