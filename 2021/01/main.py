INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/01/input"

def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(int(line))
    
    return input_list

def part1(input_list):
    answer = 0

    for i in range(len(input_list)-1):
        if input_list[i+1] > input_list[i]:
            answer += 1
    
    return answer


# part 2

def part2(input_list):
    answer = 0
    for i in range(len(input_list)-3):
        if input_list[i+3] > input_list[i]:
            answer += 1
    return answer 


def main():
    input_list = get_input()
    
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
