INPUT_FILE = "18\\input.txt"
TEST = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
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

    return [tuple(map(int, l.split(","))) for l in input_list]


def neighbors(x: int, y: int, z: int, axis=None):
    if axis == 0:
        return {(x-1, y, z), (x+1, y, z)}
    if axis == 1:
        return {(x, y-1, z), (x, y+1, z)}
    if axis == 2:
        return {(x, y, z-1), (x, y, z+1)}
    return {(x-1, y, z), (x+1, y, z),
            (x, y-1, z), (x, y+1, z),
            (x, y, z-1), (x, y, z+1)}


def part1(input_list: list[tuple[int, int, int]]):
    input_set = set(input_list)

    answer = sum(6 - len(neighbors(*p).intersection(input_set))
                 for p in input_list)
    return answer


def part2(input_list: list[tuple[int, ...]]):
    xy_dict = {}
    xz_dict = {}
    yz_dict = {}
    for x, y, z in input_list:
        if (xy := (x, y)) not in xy_dict:
            xy_dict[xy] = [z, z]
        elif z < xy_dict[xy][0]:
            xy_dict[xy][0] = z
        elif z > xy_dict[xy][1]:
            xy_dict[xy][1] = z

        if (xz := (x, z)) not in xz_dict:
            xz_dict[xz] = [y, y]
        elif y < xz_dict[xz][0]:
            xz_dict[xz][0] = y
        elif y > xz_dict[xz][1]:
            xz_dict[xz][1] = y

        if (yz := (y, z)) not in yz_dict:
            yz_dict[yz] = [x, x]
        elif x < yz_dict[yz][0]:
            yz_dict[yz][0] = x
        elif x > yz_dict[yz][1]:
            yz_dict[yz][1] = x
    input_set = set(input_list)

    def isbetween(value, range_inclusive):
        if range_inclusive is None:
            return False
        return range_inclusive[0] < value < range_inclusive[1]

    input_set = set(input_list)

    class Memoize:
        def __init__(self, f):
            self.f = f
            self.memo = {}

        def __call__(self, *args):
            if not args in self.memo:
                self.memo[args] = self.f(*args)
            return self.memo[args]

    @Memoize
    def isexteriorair(x, y, z, rec_depth=0):
        if rec_depth > 5:
            return False
        if (x, y, z) in input_set:
            return False
        if any(isexteriorair(*n, rec_depth+1) for n in neighbors(x, y, z)):
            return True
        return not all((
            isbetween(z, xy_dict.get((x, y))),
            isbetween(y, xz_dict.get((x, z))),
            isbetween(x, yz_dict.get((y, z))),
        ))

    all_ = {(p, n)
            for p in input_list for n in neighbors(*p) if isexteriorair(*n)}

    return len(all_)


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
