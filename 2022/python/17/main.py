import itertools
import copy


INPUT_FILE = "17\\input.txt"
TEST = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
""".split("\n")


def get_input(test=False):
    if test:
        return TEST

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)

    return input_list


def sanitize_input(input_list: list[str]):
    if not input_list[-1]:
        del input_list[-1]

    return input_list


bottom = [list("."*7), list("."*7), list("."*7)]
shapes = {
    "-": [list("..@@@@."), *bottom],
    "+": [list("...@..."), list("..@@@.."), list("...@..."), *bottom],
    "L": [list("....@.."), list("....@.."), list("..@@@.."), *bottom],
    "|": [list("..@...."), list("..@...."), list("..@...."), list("..@...."), *bottom],
    "#": [list("..@@..."), list("..@@..."), *bottom],
}


def part1(input_list: list[str]):
    jet_stream = itertools.cycle(input_list[0].rstrip())
    rock_cycle = itertools.cycle(shapes.values())
    tower = [["#"]*7]

    def settle_rock(rock_height):
        offset = 0

        def move_left():
            # check left
            for row in tower[offset:rock_height+offset]:
                at_index = row.index("@")
                if at_index == 0:
                    return
                if row[at_index-1] == "#":
                    return
            # move left
            for row in tower[offset:rock_height+offset]:
                for x in range(1, 7):
                    if row[x] == "@":
                        row[x-1] = "@"
                        row[x] = "."

        def move_right():
            # check right
            for row in tower[offset:rock_height+offset]:
                row = row[::-1]
                at_index = row.index("@")
                if at_index == 0:
                    return
                if row[at_index-1] == "#":
                    return
            # move right
            for row in tower[offset:rock_height+offset]:
                for x in range(6, 0, -1):
                    if row[x-1] == "@":
                        row[x] = "@"
                        row[x-1] = "."

        while True:
            # move left or right
            dir = next(jet_stream)
            if dir == ">":
                move_right()
            elif dir == "<":
                move_left()
            else:
                raise ValueError(f"{dir=}")

            # move down
            break_while = False
            for row, next_row in zip(tower[offset:offset+rock_height+1], tower[1+offset:offset+rock_height+1]):
                for i in range(7):
                    if row[i] == "@" and next_row[i] == "#":
                        break_while = True
            if break_while:
                break
            else:

                # move down tower
                for row, next_row in zip(tower[offset+rock_height -
                                               1:None if offset == 0 else offset-1:-1],
                                         tower[offset+rock_height:offset:-1]):
                    for i in range(7):
                        if row[i] == "@":
                            next_row[i] = "@"
                            row[i] = "."
                offset += 1

        for row in tower[offset:offset+rock_height]:
            for i, char in enumerate(row):
                if char == "@":
                    row[i] = "#"
        while all(c == "." for c in tower[0]):
            del tower[0]

    for _ in range(2022):
        next_rock = copy.deepcopy(next(rock_cycle))
        c = copy.deepcopy(next_rock)
        tower = [*next_rock, *tower]
        settle_rock(len(next_rock)-3)

    answer = len(tower) - 1  # minus 1 for base
    return answer


def part2(input_list: list[str]):
    jet_stream = itertools.cycle(input_list[0].rstrip())
    last_wind = None
    rock_cycle = itertools.cycle(shapes.values())
    rock_symbol_cycle = itertools.cycle(shapes)
    tower = [["#"]*7]

    def settle_rock(rock_height):
        nonlocal last_wind
        offset = 0

        def move_left():
            # check left
            for row in tower[offset:rock_height+offset]:
                at_index = row.index("@")
                if at_index == 0:
                    return
                if row[at_index-1] == "#":
                    return
            # move left
            for row in tower[offset:rock_height+offset]:
                for x in range(1, 7):
                    if row[x] == "@":
                        row[x-1] = "@"
                        row[x] = "."

        def move_right():
            # check right
            for row in tower[offset:rock_height+offset]:
                row = row[::-1]
                at_index = row.index("@")
                if at_index == 0:
                    return
                if row[at_index-1] == "#":
                    return
            # move right
            for row in tower[offset:rock_height+offset]:
                for x in range(6, 0, -1):
                    if row[x-1] == "@":
                        row[x] = "@"
                        row[x-1] = "."

        while True:
            # move left or right
            dir = next(jet_stream)
            last_wind = dir
            if dir == ">":
                move_right()
            elif dir == "<":
                move_left()
            else:
                raise ValueError(f"{dir=}")

            # move down
            break_while = False
            for row, next_row in zip(tower[offset:offset+rock_height+1], tower[1+offset:offset+rock_height+1]):
                for i in range(7):
                    if row[i] == "@" and next_row[i] == "#":
                        break_while = True
            if break_while:
                break
            else:

                # move down tower
                for row_i, row, next_row in zip(range(offset+rock_height-1, offset-1, -1),
                                                tower[offset+rock_height -
                                                      1:None if offset == 0 else offset-1:-1],
                                                tower[offset+rock_height:offset:-1]):
                    for i in range(7):
                        if row[i] == "@":
                            next_row[i] = "@"
                            row[i] = "."
                offset += 1

        for row in tower[offset:offset+rock_height]:
            for i, char in enumerate(row):
                if char == "@":
                    row[i] = "#"
        while all(c == "." for c in tower[0]):
            del tower[0]

    state_dict = {}

    remaining = 1000000000000
    result_offset = 0
    while remaining:
        next_rock = copy.deepcopy(next(rock_cycle))
        rock_symbol = next(rock_symbol_cycle)
        tower = [*next_rock, *tower]
        settle_rock(len(next_rock)-3)
        remaining -= 1
        string = rock_symbol + last_wind + \
            "".join(c for r in tower[:30] for c in r)
        if string in state_dict:
            modulus = state_dict[string][0] - remaining
            if (remaining // modulus) > 0:
                result_offset = (remaining // modulus) * \
                    (len(tower) - 1 - state_dict[string][1])
                remaining %= modulus
                print("shortcut!", remaining, modulus)
        else:
            state_dict[string] = (remaining, len(tower) - 1)
        if (n := (1000000000000 - remaining)) % 1000 == 0:
            print(n)

    answer = len(tower) - 1 + result_offset  # minus 1 for base
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
