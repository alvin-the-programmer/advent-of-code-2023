from collections import Counter


def get_lines():
    file = open("input.txt", "r")
    return file.read().split("\n")


def parse_line(line):
    game_id_str, data_str = line.split(": ")
    id_number = int(game_id_str.split(" ")[1])
    sets = data_str.split("; ")
    return id_number, [parse_set(set_str) for set_str in sets]


def parse_set(set_str):
    amounts = set_str.split(", ")
    count = dict()
    for amount in amounts:
        numeric, color = amount.split(" ")
        count[color] = int(numeric)
    return Counter(count)


def solve():
    total = 0
    for line in get_lines():
        id_number, counts = parse_line(line)
        max_blue = max(counts, key=lambda count: count["blue"])
        max_red = max(counts, key=lambda count: count["red"])
        max_green = max(counts, key=lambda count: count["green"])
        total += max_blue["blue"] * max_red["red"] * max_green["green"]
    return total
        


print(solve())

