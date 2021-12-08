import functools, operator

INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2020/03/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)
    
    return input_list


def sanitize_input(input_list):
    return [list(line.strip()) for line in input_list]


def part1(input_list):
    input_list = sanitize_input(input_list)
    return part1_calculate(input_list, 1, 3)


def part1_calculate(input_list, slope_d, slope_r):
    list_len = len(input_list)
    sublist_len = len(input_list[0])
    
    answer = len([1
        for i in range(list_len//slope_d)
        if input_list[i*slope_d][(i*slope_r) % sublist_len] == "#"
    ])

    return answer


def part2(input_list):
    slopes = (
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    )
    input_list = sanitize_input(input_list)

    answers = (part1_calculate(input_list, *s) for s in slopes)

    return functools.reduce(operator.mul, answers)


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
