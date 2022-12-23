import re
import operator
import typing
import copy
import functools
from dataclasses import dataclass
from math import gcd


INPUT_FILE = r"C:\Appl\Repos\Jonas\Advent_of_Code\2022\python\11\input.txt"
TEST_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split('\n')


@dataclass
class Monkey:
    num: int
    items: list[int]
    _operation: tuple[typing.Literal["+", "*"], str]
    _div_test: int
    _throw_to: tuple[int, int]

    def operation(self, old_val: int) -> int:
        op, argument = self._operation
        return {
            "+": operator.__add__, "*": operator.__mul__
        }[op](old_val, old_val if argument == "old" else int(argument))

    def div_test(self, test_val) -> bool:
        return test_val % self._div_test == 0

    def throw_to(self, test_val) -> int:
        return self._throw_to[int(self.div_test(test_val))]

    @staticmethod
    def from_lines(lines: list[str]):
        return Monkey(
            int(re.search(r"(\d+)", lines[0]).group(1)),
            [int(i) for i in re.findall(r"\d+", lines[1])],
            lines[2].split("new = old ")[1].split(" "),
            int(re.search(r"(\d+)", lines[3]).group(1)),
            (int(re.search(r"(\d+)", lines[5]).group(1)),
             int(re.search(r"(\d+)", lines[4]).group(1))),
        )


def get_input(test=False):
    if test:
        return TEST_INPUT

    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.rstrip('\n'))

    return input_list


def sanitize_input(input_list):
    if not input_list[-1]:
        del input_list[-1]
    monkeys = [Monkey.from_lines(input_list[i:i+6])
               for i in range(0, len(input_list), 7)]
    assert all(m.num == i for i, m in enumerate(monkeys))
    return monkeys


def part1(input_list: list[Monkey]):
    monkey_tallies = [0] * len(input_list)
    for _ in range(20):
        for monkey in input_list:
            is_ = monkey.items
            for i in range(len(is_)):
                monkey_tallies[monkey.num] += 1
                is_[i] = monkey.operation(is_[i]) // 3
                input_list[monkey.throw_to(is_[i])].items.append(is_[i])
                is_[i] = None
            monkey.items = [i for i in is_ if i is not None]
    *_, _1, _2 = sorted(monkey_tallies)
    answer = _1 * _2
    return answer


def part2(input_list: list[Monkey]):
    monkey_tallies = [0] * len(input_list)
    list_div_tests = [m._div_test for m in input_list]
    lcm = functools.reduce(operator.__mul__, list_div_tests) \
        / gcd(*list_div_tests)

    for _ in range(10_000):
        for monkey in input_list:
            is_ = monkey.items
            for i in range(len(is_)):
                monkey_tallies[monkey.num] += 1
                is_[i] = monkey.operation(is_[i]) % lcm
                input_list[monkey.throw_to(is_[i])].items.append(is_[i])
                is_[i] = None
            monkey.items = [i for i in is_ if i is not None]
    *_, _1, _2 = sorted(monkey_tallies)
    answer = _1 * _2
    return answer


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(copy.deepcopy(input_list))
    ans2 = part2(copy.deepcopy(input_list))

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
