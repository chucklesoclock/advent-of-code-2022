from utils import INPUT_DIR
import pytest
from pathlib import Path
from pprint import pprint
from collections import deque


def parse_input(path: Path) -> (list, list):
    crates = []
    rearrange_orders = []
    with path.open() as f:
        for line in f:
            if line.lstrip().startswith("["):
                i = 0
                crate_level = []
                while i < len(line):
                    crate_level.append(line[i : i + 3].strip() or None)
                    i += 4
                crates.append(crate_level)
            elif line.lstrip().startswith("1") or not line.strip():
                continue
            elif line.lstrip().startswith("move"):
                rearrange_orders.append(line.rstrip())
    # transpose list of lists to list of deques for popleft ability
    crates = list(map(deque, zip(*crates)))
    # remove Nones at beginning of each stack
    for stack in crates:
        while stack[0] is None:
            stack.popleft()
    # parse orders
    for i, order in enumerate(rearrange_orders):
        rearrange_orders[i] = parse_order(order)
    return crates, rearrange_orders


def parse_order(order: str) -> (int, int, int):
    n = int(order[len("move ") : order.index("from")])
    origin = int(order[order.index("from ") + len("from ") : order.index("to")]) - 1
    destination = int(order[order.index("to ") + len("to ") :]) - 1
    return n, origin, destination


def part1(crates, orders):
    for order in orders:
        n, origin, dest = order
        for _ in range(n):
            crates[dest].appendleft(crates[origin].popleft())
    return "".join(stack[0][1] for stack in crates)


def part2(crates, orders):
    for order in orders:
        n, origin, dest = order
        crates[dest].extendleft([crates[origin].popleft() for _ in range(n)][::-1])
    return "".join(stack[0][1] for stack in crates)


if __name__ == "__main__":
    print(part1(*parse_input(INPUT_DIR / "data05.txt")))
    print(part2(*parse_input(INPUT_DIR / "data05.txt")))


@pytest.fixture
def sample_data() -> (list, list):
    return parse_input(INPUT_DIR / "sample05.txt")


def test_part_1(sample_data):
    assert part1(*sample_data) == "CMZ"


def test_part_2(sample_data):
    assert part2(*sample_data) == "MCD"
