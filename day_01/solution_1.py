def parse_input():
    file = open("input.txt", "r")
    return file.read().split("\n")


def get_value(s):
    chars = [*s]
    first_numeric = next(char for char in chars if char.isnumeric())
    last_numeric = next(char for char in chars[::-1] if char.isnumeric())
    return int(first_numeric + last_numeric)


def solution(lines):
    return sum(get_value(line) for line in lines)

print(solution(parse_input()))
