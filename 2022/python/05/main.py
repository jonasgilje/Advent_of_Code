import copy


INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\05\input.txt"
TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".split('\n')  # noqa


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
    assert sum(i == '' for i in input_list) == 1
    separator_index = input_list.index('')
    del input_list[separator_index]

    stack_indices = [(k, v)
                     for k, v in enumerate(input_list[separator_index-1])
                     if v.strip()]
    stack_dict: dict[str, list[str]] = {v: [] for _, v in stack_indices}

    for row in input_list[separator_index-2::-1]:
        for index, label in stack_indices:
            if (char := row[index].strip()):
                stack_dict[label].append(char)

    return stack_dict, input_list[separator_index:]


def part1(stack_dict: dict[str, list[str]], input_list: list[str]):
    for row in input_list:
        _, quantity, _, source, _, destination = row.split(" ")
        quantity = int(quantity)
        temp = stack_dict[source][-quantity:]
        del stack_dict[source][-quantity:]
        stack_dict[destination].extend(temp[::-1])

    answer = "".join(list[-1] for list in stack_dict.values())
    return answer


def part2(stack_dict: dict[str, list[str]], input_list: list[str]):
    for row in input_list:
        _, quantity, _, source, _, destination = row.split(" ")
        quantity = int(quantity)
        temp = stack_dict[source][-quantity:]
        del stack_dict[source][-quantity:]
        stack_dict[destination].extend(temp)

    answer = "".join(list[-1] for list in stack_dict.values())
    return answer


def main():
    input_list = get_input(test=0)
    stack_dict, input_list = sanitize_input(input_list)
    ans1 = part1(copy.deepcopy(stack_dict), input_list)
    ans2 = part2(copy.deepcopy(stack_dict), input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
