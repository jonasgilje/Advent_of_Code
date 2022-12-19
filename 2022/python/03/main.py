import string


INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\03\input.txt"
TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
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
    return input_list


def letter_priority(char):
    return 1 + string.ascii_letters.find(char)


def split_line(line):
    middle_index = len(line) // 2
    return line[:middle_index], line[middle_index:]


def part1(input_list):
    generator = (
        letter_priority((set(_1) & set(_2)).pop())
        for _1, _2 in map(split_line, input_list)
    )
    answer = sum(generator)
    return answer


def part2(input_list):
    generator = (
        letter_priority((set(e1) & set(e2) & set(e3)).pop())
        for i in range(0, len(input_list), 3)
        for e1, e2, e3 in (input_list[i:i+3],)
    )
    answer = sum(generator)
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
