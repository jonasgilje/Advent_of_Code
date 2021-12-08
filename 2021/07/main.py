INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/07/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    first_line, = input_list
    return [int(i) for i in first_line.split(",")]


def part2(input_list):
    input_list = sanitize_input(input_list)
    min_max = (min(input_list), max(input_list))
    lowest = 0
    lowest_sum = 2 ** 31
    for i in range(*min_max):
        this_sum = sum(abs(i - j)*(abs(i-j) + 1)/2 for j in input_list)
        if this_sum < lowest_sum:
            lowest_sum = this_sum
            lowest = i

    answer = int(lowest_sum)

    return answer


def part1(input_list):
    input_list = sanitize_input(input_list)
    min_max = (min(input_list), max(input_list))
    lowest = 0
    lowest_sum = 2 ** 31
    for i in range(*min_max):
        this_sum = sum(abs(i - j)for j in input_list)
        if this_sum < lowest_sum:
            lowest_sum = this_sum
            lowest = i

    answer = lowest_sum

    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
