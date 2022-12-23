import itertools


INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\10\input.txt"
TEST_INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".split('\n')


def get_input(test=False):
    if test == 1:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


def sanitize_input(input_list: list[str]):
    if not input_list[-1]:
        del input_list[-1]
    return [i.split(" ") for i in input_list]


def part1(input_list: list[list[str]]):
    X = 1
    cycle_list = []
    for instruction in input_list:
        if instruction[0] == "noop":
            cycle_list.append(X)
        if instruction[0] == "addx":
            dx = int(instruction[1])
            cycle_list.extend((X, X))
            X += dx
    answer = sum(map(lambda x, y: (x*40 + 20) * y,
                     *zip(*enumerate(cycle_list[19::40]))))
    return answer


def part2(input_list: list[list[str]]):
    X = 1
    cycle_list = []
    for instruction in input_list:
        if instruction[0] == "noop":
            cycle_list.append(X)
        if instruction[0] == "addx":
            dx = int(instruction[1])
            cycle_list.extend((X, X))
            X += dx
    image = ["#" if abs(x - pos) <= 1 else "."
             for x, pos in zip(cycle_list, itertools.cycle(range(40)))]
    image_wrap = "\n" + "\n".join(
        "".join(image[i:i+40]) for i in range(0, len(image), 40))
    return image_wrap


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, ans2={ans2}")


if __name__ == "__main__":
    main()
