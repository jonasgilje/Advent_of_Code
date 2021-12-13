INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/12/input"


def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    return [l.split("-") for l in input_list]


def part1(input_list):
    input_list = sanitize_input(input_list)
    edge_dict = {}

    for a, b in input_list:
        if a in edge_dict:
            edge_dict[a].append(b)
        else:
            edge_dict[a] = [b]
        if b in edge_dict:
            edge_dict[b].append(a)
        else:
            edge_dict[b] = [a]
    
    complete_paths = []
    current_paths = [["start"]]

    while current_paths:
        path = current_paths.pop()
        edges = edge_dict[path[-1]]
        for edge in edges:
            if "a" <= edge[0] <= "z" and edge in path:
                continue
            new_path = [*path, edge]
            if new_path[0] == "start" and new_path[-1] == "end":
                complete_paths.append(new_path)
            else:
                current_paths.append(new_path)

    answer = len(complete_paths)
    return answer


def part2(input_list):
    input_list = sanitize_input(input_list)
    edge_dict = {}

    for a, b in input_list:
        if a in edge_dict:
            edge_dict[a].append(b)
        else:
            edge_dict[a] = [b]
        if b in edge_dict:
            edge_dict[b].append(a)
        else:
            edge_dict[b] = [a]
    
    small_caves = edge_dict.keys()
    small_caves = [c for c in small_caves if "a" <= c[0] <= "z" and c not in ("start", "end")]
    complete_paths = []

    for okay_visit_twice in small_caves:
        
        current_paths = [["start"]]
        
        while current_paths:
            path = current_paths.pop()
            edges = edge_dict[path[-1]]
            for edge in edges:
                if edge == okay_visit_twice:
                    if len([edge for e in path if e == edge]) > 1:
                        continue
                else:
                    if "a" <= edge[0] <= "z" and edge in path:
                        continue
                
                new_path = [*path, edge]
                if new_path[0] == "start" and new_path[-1] == "end":
                    if new_path not in complete_paths:
                        complete_paths.append(new_path)
                else:
                    current_paths.append(new_path)

    answer = len(complete_paths)
    return answer



def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    #ans1=5958, ans2=150426
    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
