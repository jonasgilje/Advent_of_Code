INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/10/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    pass


def part1(input_list):
    answer = 0
    conv_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    point_dict = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    for line in input_list:
        stack = []
        for char in line:
            if char in conv_dict:
                top_char = stack.pop()
                if conv_dict[char] != top_char:
                    answer += point_dict[char]
                    break
            else:
                stack.append(char)

    return answer



def part2(input_list):
    conv_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    conv_dict_2 = {v: k for k, v in conv_dict.items()}
    point_dict = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    
    score_list = []

    for line in input_list:
        stack = []
        for char in line:
            if char in conv_dict:
                top_char = stack.pop()
                if conv_dict[char] != top_char:
                    break
            else:
                stack.append(char)
        else:
            score = 0
            if stack:
                rev = [conv_dict_2[c] for c in stack[::-1]]
                for char in rev:
                    score *= 5
                    score += point_dict[char]
            score_list.append(score)
    
    answer = sorted(score_list)[len(score_list) // 2]

    return answer



def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
