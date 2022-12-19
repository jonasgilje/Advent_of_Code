INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\02\input.txt"
TEST_INPUT = """A Y
B X
C Z
""".split('\n')


def get_input(test=False):
    if test:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


def sanitize_input(input_list):
    if not input_list[-1]:
        del input_list[-1]
    return [i.split(" ") for i in input_list]


def part1(input_list):
    def game(arg1, arg2):
        score = "XYZ".find(arg2) + 1
        score += [3, 6, 0][("XYZ".find(arg2) - "ABC".find(arg1)) % 3]
        return score
    answer = sum(game(*i) for i in input_list)
    return answer


def part2(input_list):
    def game(arg1, arg2):
        score = "XYZ".find(arg2) * 3
        score += ("ABC".find(arg1) + "XYZ".find(arg2) - 1) % 3 + 1
        return score
    answer = sum(game(*i) for i in input_list)
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
