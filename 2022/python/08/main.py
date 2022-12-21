INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\08\input.txt"
TEST_INPUT = """30373
25512
65332
33549
35390
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
    input_list = [[int(i) for i in line] for line in input_list]
    return input_list


def part1(input_list: list[list[int]]):
    visible = set()
    transposed = zip(*input_list)
    for flip, outer_list in enumerate((input_list, transposed)):
        for row_no, line in enumerate(outer_list):
            from_left = list(enumerate(line))
            from_right = from_left[::-1]
            for list_ in (from_left, from_right):
                highest = -1
                for col_no, height in list_:
                    if height > highest:
                        highest = height
                        pos = (row_no, col_no) if not flip else \
                              (col_no, row_no)
                        visible.add(pos)

    answer = len(visible)
    return answer


def part2(input_list: list[list[int]]):
    scenic_factors = {}
    transposed = zip(*input_list)
    for flip, outer_list in enumerate((input_list, transposed)):
        for row_no, line in enumerate(outer_list):
            from_left = list(enumerate(line))
            from_right = from_left[::-1]
            for list_ in (from_left, from_right):
                seen_heights = {}
                for index, (col_no, height) in enumerate(list_):
                    pos = (row_no, col_no) if not flip else \
                          (col_no, row_no)
                    if pos not in scenic_factors:
                        scenic_factors[pos] = 1

                    scenic_factors[pos] *= index - \
                        max((i for h, i in seen_heights.items()
                             if h >= height), default=0)

                    seen_heights[height] = index

    answer = max(scenic_factors.values())
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
