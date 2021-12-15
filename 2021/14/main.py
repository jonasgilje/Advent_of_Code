INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/14/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    start_string, _, *rest = input_list
    return start_string, [s.split(" -> ") for s in rest]


def part1(input_list):
    start_string, rules = sanitize_input(input_list)

    rule_dict = {k: v + k[1] for k, v in rules}

    for _ in range(10):
        new_string = start_string[0]
        for i in range(len(start_string)-1):
            if start_string[i:i+2] in rule_dict:
                new_string += rule_dict[start_string[i:i+2]]
            else:
                new_string += start_string[i+1]
        start_string = new_string

    count_dict = {}

    for c in start_string:
        if c not in count_dict:
            count_dict[c] = 0
        count_dict[c] += 1

    answer = max(count_dict.values()) - min(count_dict.values())
    
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
