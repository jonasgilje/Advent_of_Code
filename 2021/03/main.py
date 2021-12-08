import functools, operator, itertools

INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/03/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(list(line.strip()))
    
    return input_list


def sanitize_input(input_list):
    pass 


def part1(input_list):
    hor_dim = len(input_list[0])
    gamma_rate = []
    epsilon_rate = []

    for i in range(hor_dim):
        num_zeros = num_ones = 0
        for l in input_list:
            if l[i] == "0":
                num_zeros += 1
            elif l[i] == "1":
                num_ones += 1
        if num_zeros > num_ones:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")

    gamma_rate_int = int("".join(gamma_rate), 2)
    epsilon_rate_int = int("".join(epsilon_rate), 2)

    return gamma_rate_int * epsilon_rate_int


def part2(input_list):
    hor_dim = len(input_list[0])
    oxy_list = input_list[:]
    co2_list = input_list[:]

    for i in range(hor_dim):
        if len(oxy_list) <= 1:
            break
        num_zeros = num_ones = 0
        for l in oxy_list:
            if l[i] == "0": num_zeros += 1
            else: num_ones += 1
        if num_ones == num_zeros:
            num_ones += 1  # tiebreak
        char = "0" if num_zeros > num_ones else "1"
        oxy_list = [l for l in oxy_list if l[i] == char]


    for i in range(hor_dim):
        if len(co2_list) <= 1:
            break
        num_zeros = num_ones = 0
        for l in co2_list:
            if l[i] == "0": num_zeros += 1
            
            else: num_ones += 1
        if num_ones == num_zeros:
            num_ones += 1  # tiebreak
        char = "0" if num_zeros < num_ones else "1"
        co2_list = [l for l in co2_list if l[i] == char]


    return int("".join(oxy_list[0]), 2) * int("".join(co2_list[0]), 2)


def main():
    input_list = get_input()

    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
