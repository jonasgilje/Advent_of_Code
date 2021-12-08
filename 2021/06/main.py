INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/06/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)
    
    return input_list


def sanitize_input(input_list):
    first_line, = input_list
    return [int(i) for i in first_line.split(",")]


def part1(input_list):
    input_list = sanitize_input(input_list)

    for _ in range(80):
        for i in range(len(input_list)):
            if input_list[i] == 0:
                input_list[i] = 6
                input_list.append(8)
            else:
                input_list[i] -= 1

    answer = len(input_list)
    return answer


def part2(input_list):
    input_list = sanitize_input(input_list)

    input_dict = {k: 0 for k in range(9)}

    for i in input_list:
        input_dict[i] += 1

    for _ in range(256):
        num_zeros = input_dict[0]
        for i in range(1, 9):
            input_dict[i-1] = input_dict[i]
        input_dict[6] += num_zeros
        input_dict[8] = num_zeros

    answer = sum(input_dict.values())
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
