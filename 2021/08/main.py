INPUT_FILE = "/home/jonasgilje/Documents/Advent_of_Code/2021/08/input"

# 1: 2 segments
# 7: 3 segments
# 4: 4 segments
# 8: 7 segments

def get_input():
    input_list = []

    with open(INPUT_FILE, "r") as file:
        for line in file:
            input_list.append(line.strip())
    
    return input_list


def sanitize_input(input_list):
    delimited = [tuple(sl.split(" ")  for sl in l.split(" | ")) for l in input_list]
    return delimited



def part1(input_list):
    sanitized = sanitize_input(input_list)
    right_part = (len(i) for l in sanitized for i in l[1])
    answer = 0
    for i in right_part:
        if i in (2, 3, 4, 7):
            answer += 1
    
    return answer


def part2(input_list):
    sanitized = sanitize_input(input_list)

    conv_to_digits = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    
    answer = 0 
    for line in sanitized:
        left_part, right_part = line
        
        lengths = [len(s) for s in left_part]
        one_seven_four_eight_idx = [lengths.index(i) for i in (2, 3, 4, 7)]
        one, seven, four, eight = [left_part[idx] for idx in one_seven_four_eight_idx]

        segment = {}

        for c in seven:
            if c not in one:
                segment["a"] = c
                break
        

        count_dict = {k: 0 for k in "abcdefg"}
        for c in "".join(left_part):
            count_dict[c] += 1


        for c in "abcdefg":
            if all((
                c not in one,
                c not in four,
                c not in seven,
            )):
                if count_dict[c] == 4:
                    segment["e"] = c
                elif count_dict[c] == 7:
                    segment["g"] = c
            elif all((
                c not in one,
                c in four,
                c not in seven,
            )):
                if count_dict[c] == 6:
                    segment["b"] = c
                elif count_dict[c] == 7:
                    segment["d"] = c
        
       

        for c in "abcdefg":
            if c in segment.values(): 
                continue
            if count_dict[c] == 8:
                segment["c"] = c
            elif count_dict[c] == 9:
                segment["f"] = c

        segment_flipped = {v: k for k, v in segment.items()}
        sanitized_right_part = [
            conv_to_digits["".join(sorted("".join([segment_flipped[c] for c in l])))] for l in right_part
        ]
        
        answer += int("".join(map(str,sanitized_right_part)))

    return answer


def main():
    input_list = get_input()
    ans1 = part1(input_list)
    ans2 = part2(input_list)

    print(f"{ans1=}, {ans2=}")


if __name__ == "__main__":
    main()
