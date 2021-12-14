#INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/04/input"
INPUT_FILE = "C:\\Users\\1jona\\Documents\\GitHub\\Advent_of_Code\\2021\\14\\input"

def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    pass


def part1(input_list):
    print(input_list)
    answer = None
    return answer


def part2(input_list):

    answer = None
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
