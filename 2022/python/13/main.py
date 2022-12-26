import functools


INPUT_FILE = "13\\input.txt"
TEST = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".split("\n")


def get_input(test=False):
    if test:
        return TEST

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line)

    return input_list


def sanitize_input(input_list):
    if not input_list[-1]:
        del input_list[-1]
    return input_list


def part1(input_list: list[str]):
    global compare

    def compare(left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return None
            return left < right
        elif isinstance(left, list) and isinstance(right, list):
            for i1, i2 in zip(left, right):
                if (c := compare(i1, i2)) is not None:
                    return c
            return compare(len(left), len(right))
        elif isinstance(left, int) and isinstance(right, list):
            return compare([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return compare(left, [right])

    answer = sum(i
                 for i, (l, r) in enumerate(zip(input_list[::3], input_list[1::3]), start=1)
                 if compare(eval(l), eval(r)))

    return answer


def part2(input_list: list[str]):
    @functools.cmp_to_key
    def new_compare(left, right):
        return {True: 1, None: 0, False: -1}[compare(left, right)]

    lines = [eval(l) for l in input_list if l.strip()]
    lines.extend(([[2]], [[6]]))
    lines.sort(key=new_compare, reverse=True)
    first = lines.index([[2]])
    second = lines.index([[6]])
    answer = (first+1) * (second+1)
    return answer


def main():
    input_list = get_input(test=1)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
