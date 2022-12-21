INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\06\input.txt"
TEST_INPUT = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
""".split('\n')


def get_input(test=False):
    if test:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


def sanitize_input(input_list: list[str]):
    if not input_list[-1]:
        del input_list[-1]
    return input_list


def part1(input_list: list[str]):
    def find_marker(string, w_size=4):
        for i in range(w_size, len(string)):
            if len(set(string[i-w_size:i])) == w_size:
                return i
    answer = [find_marker(i) for i in input_list]
    return answer


def part2(input_list: list[str]):
    def find_marker(string, w_size=14):
        for i in range(w_size, len(string)):
            if len(set(string[i-w_size:i])) == w_size:
                return i
    answer = [find_marker(i) for i in input_list]
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
