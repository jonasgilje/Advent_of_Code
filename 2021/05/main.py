INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/05/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    new_list = []
    for line in input_list:
        x1y1, x2y2 = line.split(" -> ")
        string_tuple = (*x1y1.split(","), *x2y2.split(","))
        new_list.append(tuple(int(i) for i in string_tuple))
    return new_list


def part1(input_list):
    sanitized = sanitize_input(input_list)
    filtered = [t for t in sanitized if t[0] == t[2] or t[1] == t[3]]
    count_dict = {}
    for t in filtered:
        x1, y1, x2, y2 = t
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                if (x1, i) not in count_dict:
                    count_dict[(x1, i)] = 0
                count_dict[(x1, i)] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                if (i, y1) not in count_dict:
                    count_dict[(i, y1)] = 0
                count_dict[(i, y1)] += 1
    
    answer = 0
    for i in count_dict.values():
        if i >= 2:
            answer += 1

    return answer


def part2(input_list):
    sanitized = sanitize_input(input_list)

    count_dict = {}
    for t in sanitized:
        x1, y1, x2, y2 = t
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                if (x1, i) not in count_dict:
                    count_dict[(x1, i)] = 0
                count_dict[(x1, i)] += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                if (i, y1) not in count_dict:
                    count_dict[(i, y1)] = 0
                count_dict[(i, y1)] += 1
        else:
            if x1 > x2:
                x1, x2, y1, y2 = x2, x1, y2, y1
            y_sign = 1 if y1 < y2 else -1
            for i, j in zip(range(x1, x2+1), range(y1, y2+y_sign, y_sign)):
                if (i, j) not in count_dict:
                    count_dict[(i, j)] = 0
                count_dict[(i, j)] += 1
            
    
    answer = 0
    for i in count_dict.values():
        if i >= 2:
            answer += 1
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
