INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\04\input.txt"
TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
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
    input_list = [tuple(tuple(map(int, sl.split("-"))) for sl in i.split(","))
                  for i in input_list]
    return input_list


def part1(input_list):
    def overlapping(line_tuple) -> bool:
        (s1, e1), (s2, e2) = line_tuple
        return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)
    answer = sum(map(overlapping, input_list))
    return answer


def part2(input_list):
    def overlapping(line_tuple) -> bool:
        (s1, e1), (s2, e2) = line_tuple
        return min(e1, e2) >= max(s1, s2)
    answer = sum(map(overlapping, input_list))
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
