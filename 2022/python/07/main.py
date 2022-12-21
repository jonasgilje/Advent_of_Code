INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\07\input.txt"
TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".split('\n')


def get_input(test=False):
    if test:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


class FSNode:
    def __init__(self, name: str, type: str, size: int = None):
        self.name = name
        self.__size = size
        assert type in ("dir", "file")
        self.type = type
        self.children: dict[str, FSNode] = {}

    def add_child(self, node: "FSNode"):
        assert self.type == "dir"
        self.children[node.name] = node

    @property
    def size(self):
        if self.__size is not None:
            return self.__size
        assert self.type == "dir"
        self.__size = sum(n.size for n in self.children.values())
        return self.__size

    def walk_dir(self):
        assert self.type == "dir"
        for node in self.children.values():
            if node.type == "dir":
                yield node
                yield from node.walk_dir()


def sanitize_input(input_list: list[str]):
    if not input_list[-1]:
        del input_list[-1]
    assert input_list[0] == "$ cd /"
    del input_list[0]

    root_node = FSNode("/", "dir")
    pwd_stack = [root_node]

    for line in input_list:
        if line.startswith("$ cd "):
            _, dir_name = line.split("$ cd ")
            if dir_name == "..":
                del pwd_stack[-1]
            else:
                pwd_stack.append(pwd_stack[-1].children[dir_name])
        if not line.startswith("$"):
            size, name = line.split(" ")

            pwd_stack[-1].add_child(
                FSNode(name, "dir" if size == "dir" else "file",
                             None if size == "dir" else int(size)))

    return root_node


def part1(input_list: FSNode):
    answer = sum(s for node in input_list.walk_dir()
                 if (s := node.size) < 100_000)
    return answer


def part2(input_list: FSNode):
    size_limit = 70_000_000
    needed_space = 30_000_000
    need_to_free = needed_space - (size_limit - input_list.size)

    answer = min(s for node in input_list.walk_dir()
                 if (s := node.size) >= need_to_free)
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
