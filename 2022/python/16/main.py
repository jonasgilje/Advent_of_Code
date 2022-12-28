import re


INPUT_FILE = "16\\input.txt"
TEST = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
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

    valves = [(
        re.search("Valve ([A-Z]+) has", l).group(1),
        int(re.search("rate=(\d+);", l).group(1)),
        l.split("to valve")[1].strip("s \n").split(", ")
    ) for l in input_list]

    return ({valve: rate for valve, rate, _ in valves},
            {valve: dests for valve, _, dests in valves})


def part1(input_dicts: tuple[dict[str, int], dict[str, list[str]]]):
    rates, destinations = input_dicts
    valves = list(rates)
    # dists[valves.index(v1)][valves.index(v2)] = distance
    distances = [[None] * len(valves) for _ in range(len(valves))]

    for i, valve in enumerate(valves):
        stack = [(0, valve)]
        while any(d is None for d in distances[i]):
            curr_dist, curr_valve = stack.pop(0)
            curr_dist += 1
            for curr_dest in destinations[curr_valve]:
                if distances[i][valves.index(curr_dest)] is not None:
                    continue
                distances[i][valves.index(curr_dest)] = curr_dist
                stack.append((curr_dist, curr_dest))

    nonzeros = {v: r for v, r in rates.items() if r != 0}

    # minutes, curr index, open valves, total score
    steps = [(30, valves.index("AA"), set(), 0)]
    max_score = 0

    while steps:
        minutes_left, current_valve_index, open_valves, total_score = steps.pop()
        candidate_steps = [
            (
                open_minutes,
                valves.index(v),
                open_valves | {v},
                (total_score + open_minutes*r)
            )
            for v, r in nonzeros.items() if v not in open_valves and
            (open_minutes := (minutes_left - distances[current_valve_index][valves.index(v)] - 1)) > 0]
        steps.extend(candidate_steps)

        for *_, score in candidate_steps:
            if score > max_score:
                max_score = score

    return max_score


def part2(input_dicts: tuple[dict[str, int], dict[str, list[str]]]):
    rates, destinations = input_dicts
    valves = list(rates)
    # dists[valves.index(v1)][valves.index(v2)] = distance
    distances = [[None] * len(valves) for _ in range(len(valves))]

    for i, valve in enumerate(valves):
        stack = [(0, valve)]
        while any(d is None for d in distances[i]):
            curr_dist, curr_valve = stack.pop(0)
            curr_dist += 1
            for curr_dest in destinations[curr_valve]:
                if distances[i][valves.index(curr_dest)] is not None:
                    continue
                distances[i][valves.index(curr_dest)] = curr_dist
                stack.append((curr_dist, curr_dest))

    nonzeros = {v: r for v, r in rates.items() if r != 0}

    # minutes, curr index, open valves, total score
    steps = [(26, valves.index("AA"), set(), 0)]
    max_score = 0
    finished: dict[frozenset, int] = {}

    while steps:
        minutes_left, current_valve_index, open_valves, total_score = steps.pop()
        new_steps = []
        for v, r in nonzeros.items():
            if v in open_valves:
                continue
            if (open_minutes := (minutes_left - distances[current_valve_index][valves.index(v)] - 1)) <= 0:
                continue
            new_steps.append((
                open_minutes,
                valves.index(v),
                open_valves | {v},
                (total_score + open_minutes*r)
            ))

        steps.extend(new_steps)

        for *_, open_valves, score in new_steps:
            fr = frozenset(open_valves)
            if finished.get(fr, 0) < score:
                finished[fr] = score

    max_score = 0

    finished_items = list(finished.items())

    for i, (fs1, s1) in enumerate(finished_items):
        for (fs2, s2) in finished_items[:i]:
            if fs1.isdisjoint(fs2):
                if max_score < s1 + s2:
                    max_score = s1 + s2

    return max_score


def main():
    input_list = get_input(test=0)
    input_list = sanitize_input(input_list)
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
