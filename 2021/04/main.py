import copy

INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/04/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip())
    
    return input_list


def sanitize_input(input_list):
    first_line, _, *rest = input_list
    numbers = [int(i) for i in first_line.split(",")]
    boards = []

    for i in range(0, len(rest), 6):
        boards.append(rest[i:i+5])
    
    for i in range(len(boards)):
        for j in range(5):
            new_sub_sub_list = []
            for k in range(5):
                new_sub_sub_list.append(int(boards[i][j][k*3:k*3+2]))
            boards[i][j] = new_sub_sub_list
    
    return numbers, boards


def check_board(board):
    new_board = []
    for l in board:
        for i in l:
            new_board.append(i)
    board = new_board

    for i in range(5):
        if all((
            board[i*5+j] == "X" for j in range(5)
        )):
            return True
    for i in range(5):
        if all((
            board[i+j*5] == "X" for j in range(5)
        )):
            return True
    
    return False


def part1(input_list):
    num, boa = sanitize_input(input_list)
    marked_boards = copy.deepcopy(boa)

    try:
        for n in num:
            for board_i in range(len(marked_boards)):
                
                for j in range(5):
                    for k in range(5):
                        if marked_boards[board_i][j][k] == n:
                            marked_boards[board_i][j][k] = "X"
                if check_board(marked_boards[board_i]):
                    raise StopIteration
    except StopIteration:
        pass
    
    unmarked_sum = 0

    board = marked_boards[board_i]

    for l in board:
        for m in l:
            if m != "X":
                unmarked_sum += m

    answer = unmarked_sum * n
    return answer


def part2(input_list):

    num, boa = sanitize_input(input_list)
    marked_boards = copy.deepcopy(boa)

    won_boards = []

    try:
        for n in num:
            for board_i in range(len(marked_boards)):
                if board_i in won_boards:
                    continue
                for j in range(5):
                    for k in range(5):
                        if marked_boards[board_i][j][k] == n:
                            marked_boards[board_i][j][k] = "X"
                if check_board(marked_boards[board_i]):
                    won_boards.append(board_i)
                    if len(won_boards) == len(boa):
                        raise StopIteration
    except StopIteration:
        pass

 
    unmarked_sum = 0

    board = marked_boards[board_i]

    for l in board:
        for m in l:
            if m != "X":
                unmarked_sum += m

    answer = unmarked_sum * n
    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
