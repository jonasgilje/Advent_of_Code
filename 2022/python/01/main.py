INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\01\input.txt"
TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
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
    ...


def part1(input_list):
    answer = max(sum(map(int, sublist.split(",")))
                 for sublist in ",".join(input_list).rstrip(",").split(",,"))
    return answer


def part2(input_list):
    answer = sum(sorted((sum(map(int, sublist.split(",")))
                         for sublist
                         in ",".join(input_list)
                               .rstrip(",")
                               .split(",,")), reverse=True)[:3])
    return answer


def main():
    input_list = get_input(test=0)
    # input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
