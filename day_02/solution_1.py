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


def contains(container, contained):
    return all(container[x] >= contained[x] for x in contained)


LIMIT = Counter({"red": 12, "green": 13, "blue": 14})


def solve():
    total = 0
    for line in get_lines():
        id_number, counts = parse_line(line)
        game_possible = True
        for count in counts:
            if not contains(LIMIT, count):
                game_possible = False
                break
        if game_possible:
            total += id_number
    return total


print(solve())
