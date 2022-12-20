from utils import INPUT_DIR


def part1():
    assignments_gen = get_assignments_gen()
    return sum(1 for asses in assignments_gen if fully_contains(*asses))


def part2():
    return sum(1 for asses in get_assignments_gen() if somewhat_contains(*asses))


def get_assignments_gen():
    assignments_gen = (
        [tuple(map(int, x.split("-"))) for x in line.split(",")]
        for line in (INPUT_DIR / "data04").read_text().splitlines()
    )

    return assignments_gen


def fully_contains(assignment_1, assignment_2):
    a, b = assignment_1
    c, d = assignment_2
    return (c <= a and b <= d) or (a <= c and d <= b)


def somewhat_contains(assignment_1, assignment_2):
    a, b = assignment_1
    c, d = assignment_2
    return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d


if __name__ == "__main__":
    print(part1())
    print(part2())
