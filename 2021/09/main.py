INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/09/input"


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
    dim_x, dim_y = len(input_list[0]), len(input_list)

    answer = 0

    for y in range(dim_y):
        for x in range(dim_x):
            if x != 0:
                if input_list[y][x-1] <= input_list[y][x]:
                    continue
            if y != 0:
                if input_list[y-1][x] <= input_list[y][x]:
                    continue
            if x + 1 != dim_x:
                if input_list[y][x+1] <= input_list[y][x]:
                    continue
            if y + 1 != dim_y:
                if input_list[y+1][x] <= input_list[y][x]:
                    continue
            answer += 1 + input_list[y][x]
            
    return answer


def part2(input_list):
    input_list = sanitize_input(input_list)
    dim_x, dim_y = len(input_list[0]), len(input_list)

    low_point_list = []

    for y in range(dim_y):
        for x in range(dim_x):
            if x != 0:
                if input_list[y][x-1] <= input_list[y][x]:
                    continue
            if y != 0:
                if input_list[y-1][x] <= input_list[y][x]:
                    continue
            if x + 1 != dim_x:
                if input_list[y][x+1] <= input_list[y][x]:
                    continue
            if y + 1 != dim_y:
                if input_list[y+1][x] <= input_list[y][x]:
                    continue
            low_point_list.append((x, y))
    
    def next_iter(edge, basin):
        new_edge = []
        for x, y in edge:
            if x != 0:
                if 9 != input_list[y][x-1] >= input_list[y][x] \
                    and (x-1, y) not in basin and (x-1, y) not in new_edge:
                    new_edge.append((x-1, y))
            if y != 0:
                if 9 != input_list[y-1][x] >= input_list[y][x] \
                    and (x, y-1) not in basin and (x, y-1) not in new_edge:
                    new_edge.append((x, y-1))
            if x + 1 != dim_x:
                if 9 != input_list[y][x+1] >= input_list[y][x] \
                    and (x+1, y) not in basin and (x+1, y) not in new_edge:
                    new_edge.append((x+1, y))
            if y + 1 != dim_y:
                if 9 != input_list[y+1][x] >= input_list[y][x] \
                    and (x, y+1) not in basin and (x, y+1) not in new_edge:
                    new_edge.append((x, y+1))
        new_basin = basin + edge
        return new_edge, new_basin
    
    top_three = []

    for l_p in low_point_list:
        edge, basin = [l_p], []
        while edge:
            edge, basin = next_iter(edge, basin)
        
        l = len(basin)
        top_three = sorted([*top_three, l])[::-1][:3]

    answer = top_three[0] * top_three[1] * top_three[2]
    
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
