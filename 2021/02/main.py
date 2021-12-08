INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/02/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            command, number = line.split(" ")
            input_list.append((command, int(number)))
    
    return input_list


def sanitize_input(input_list):
    pass


def part1(input_list):
    forward = 0
    depth = 0

    for cmd, num in input_list:
        if cmd == "forward":
            forward += num
        elif cmd == "down":
            depth += num
        elif cmd == "up":
            depth -= num


    return forward * depth


def part2(input_list):
    aim = 0
    forward = 0
    depth = 0

    for cmd, num in input_list:
        if cmd == "forward":
            forward += num
            depth += aim * num
        elif cmd == "down":
            aim += num
        elif cmd == "up":
            aim -= num


    return forward * depth


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
