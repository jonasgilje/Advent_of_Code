import itertools

INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/11/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    return [[int(i) for i in l] for l in input_list]


def part1(input_list):
    input_list = sanitize_input(input_list)

    dir = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    def flash(x, y, has_flashed):
        if (x, y) in has_flashed:
            return
        has_flashed.append((x, y))

        input_list[y][x] = 0
        for d_x, d_y in dir:
            try:
                if x + d_x < 0 or y + d_y < 0:
                    continue
                input_list[y + d_y][x + d_x] += 1
            except IndexError:
                pass
    
    def flash_list(grid):
        return [(x, y) for x, y in itertools.product(range(10), range(10)) if grid[y][x] > 9]


    answer = 0

    for _ in range(100):
        has_flashed = []

        for x, y in itertools.product(range(10), range(10)):
            input_list[y][x] += 1
        while f_l := flash_list(input_list):
            for t in f_l:
                flash(*t, has_flashed)
                answer += 1
        for x, y in has_flashed:
            input_list[y][x] = 0
        
                            


    return answer


def part2(input_list):
    input_list = sanitize_input(input_list)

    dir = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    def flash(x, y, has_flashed):
        if (x, y) in has_flashed:
            return
        has_flashed.append((x, y))

        input_list[y][x] = 0
        for d_x, d_y in dir:
            try:
                if x + d_x < 0 or y + d_y < 0:
                    continue
                input_list[y + d_y][x + d_x] += 1
            except IndexError:
                pass
    
    def flash_list(grid):
        return [(x, y) for x, y in itertools.product(range(10), range(10)) if grid[y][x] > 9]


    answer = 0

    while True:
        answer += 1
        has_flashed = []

        for x, y in itertools.product(range(10), range(10)):
            input_list[y][x] += 1
        while f_l := flash_list(input_list):
            for t in f_l:
                flash(*t, has_flashed)
        for x, y in has_flashed:
            input_list[y][x] = 0
        flattened = [i for l in input_list for i in l if i == 0]
        if len(flattened) == 100:
            break
                    
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
