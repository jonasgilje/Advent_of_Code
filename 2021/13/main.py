import itertools

INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/13/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    idx = input_list.index("")
    dots = [tuple(map(int, t)) for t in [l.split(",") for l in input_list[:idx]]]
    folds = [(a[-1], int(b)) for a, b in [l.split("=") for l in input_list[idx+1:]]]
    return dots, folds


def part1(input_list):
    dots, folds = sanitize_input(input_list)
    max_x, max_y = max(d[0] for d in dots), max(d[1] for d in dots)

    fold = folds[0]
    dots = [((a, b) if a < fold[1] else (max_x-a, b)) for a, b in dots]
    #dots = [((a, b) if b < fold[1] else (a, max_y-b)) for a, b in dots]

    max_x, max_y = max(d[0] for d in dots), max(d[1] for d in dots)

    answer = 0
    dot_set = set(dots)
    for x, y in itertools.product(range(max_x+1), range(max_y+1)):
        if (x, y) in dot_set:
            answer += 1

    return answer


def part2(input_list):
    dots, folds = sanitize_input(input_list)

    for fold in folds:
        
        if fold[0] == "x":
            dots = [((a, b) if a < fold[1] else (fold[1]*2-a, b)) for a, b in dots]
        else:
            dots = [((a, b) if b < fold[1] else (a, fold[1]*2-b)) for a, b in dots]
    
    max_x, max_y = max(d[0] for d in dots), max(d[1] for d in dots)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print("#" if (x, y) in dots else " ", end="")
        print()
    
    answer = None

    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
