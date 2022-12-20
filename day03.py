import pytest
from utils import INPUT_DIR
from string import ascii_letters
import itertools
import functools


def yield_input_data():
    with (INPUT_DIR / "data03").open() as f:
        for line in f:
            yield line.rstrip("\n")


def part1(data):
    priority_sum = 0
    for rucksack in data:
        common_items = set(rucksack[: (mid := len(rucksack) // 2)]).intersection(
            set(rucksack[mid:])
        )
        priority_sum += sum(priority(item) for item in common_items)
    return priority_sum


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return itertools.zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


def part2(data):
    priority_sum = 0
    for elf_group in data:
        common_items = functools.reduce(set.intersection, map(set, elf_group))
        priority_sum += sum(priority(item) for item in common_items)
    return priority_sum


def priority(letter: str) -> int:
    try:
        return ascii_letters.index(letter) + 1
    except ValueError:
        raise ValueError(f"{letter=} not in {ascii_letters=}")


if __name__ == "__main__":
    print(part1(yield_input_data()))
    print(part2(grouper(yield_input_data(), 3, incomplete="strict")))


@pytest.fixture
def sample_data():
    return (INPUT_DIR / "sample03").read_text().splitlines()


def test_part_1(sample_data):
    assert part1(sample_data) == 157


def test_part_2(sample_data):
    assert part2(grouper(sample_data, 3, incomplete="strict")) == 70
