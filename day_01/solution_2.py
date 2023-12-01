def parse_input():
    file = open("input.txt", "r")
    return file.read().split("\n")


def get_first_numeric(s, words):
    for i in range(len(s)):
        if s[i].isnumeric():
            return s[i]
        else:
            for word, value in words.items():
                if s[i:].startswith(word):
                    return value


def get_value(s):
    first_numeric = get_first_numeric(
        s,
        {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        },
    )
    last_numeric = get_first_numeric(
        s[::-1],
        {
            "eno": "1",
            "owt": "2",
            "eerht": "3",
            "ruof": "4",
            "evif": "5",
            "xis": "6",
            "neves": "7",
            "thgie": "8",
            "enin": "9",
        },
    )
    return int(first_numeric + last_numeric)


def solution(lines):
    return sum(get_value(line) for line in lines)


print(solution(parse_input()))
