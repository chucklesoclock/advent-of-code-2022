import pytest
from utils import INPUT_DIR
from string import ascii_letters


def yield_data():
    with (INPUT_DIR / "data03").open() as f:
        for line in f:
            yield line


def part1(data):
    priority_sum = 0
    for rucksack in data:
        common_items = set(rucksack[: (mid := len(rucksack) // 2)]).intersection(
            set(rucksack[mid:])
        )
        priority_sum += sum(priority(item) for item in common_items)
    return priority_sum


def priority(letter: str) -> int:
    try:
        return ascii_letters.index(letter) + 1
    except ValueError:
        raise ValueError(f"{letter} not in {ascii_letters=}")


if __name__ == "__main__":
    print(part1(yield_data()))


@pytest.fixture
def sample_data():
    return (INPUT_DIR / "sample03").read_text().splitlines()


def test_part_1(sample_data):
    assert part1(sample_data) == 157
