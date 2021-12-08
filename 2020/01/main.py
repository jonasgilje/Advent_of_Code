INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2020/01/input"

def get_input():

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(int(line))
    
    return input_list

def part1(input_list):
    input_set = set(input_list)

    for number in input_list:
        if 2020 - number in input_set:
            break
    
    return number * (2020-number)


# part 2

def part2(input_list):
    input_len = len(input_list)
    input_set = set(input_list)

    pair_of_two_less_than_2020_dict = {}

    for i in range(input_len):
        for j in range(i, input_len):
            num_1 = input_list[i]
            num_2 = input_list[j]
            sum = num_1 + num_2
            if sum < 2020:
                pair_of_two_less_than_2020_dict[sum] = num_1 * num_2

    for k, v in pair_of_two_less_than_2020_dict.items():
        if 2020 - k in input_set:
            break

    return (2020-k) * v 


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
