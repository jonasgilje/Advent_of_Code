INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2020/02/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)
    
    return input_list


def sanitize_input(input_list):
    input_split_once = (
        tuple(line.split(":"))
        for line in input_list
    )
    input_split_twice = (
        (*item1.split(" "), item2.strip())
        for item1, item2 in input_split_once
    )
    input_split_thrice = (
        (*(int(i) for i in item1.split("-")), *rest)
        for item1, *rest in input_split_twice
    )
    return input_split_thrice


def part1(input_list):
    input_split_thrice = sanitize_input(input_list)

    answer = len([
        1 for range_start, range_end, character, password in input_split_thrice
        if range_start <= len([c for c in list(password) if c == character]) <= range_end
    ])

    return answer


def part2(input_list):
    input_split_thrice = sanitize_input(input_list)

    answer = len([
        1 for first_position, second_position, character, password in input_split_thrice
        if all((
            password[first_position-1] != password[second_position-1],
            password[first_position-1] == character or
            password[second_position-1] == character
        ))
    ])

    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
