from typing import Dict, Tuple


def display_range(input: Dict[Tuple[int, int], int]):
    print("Range, Readings")

    for ranges, count in input.items():
        print(f"{ranges[0]}-{ranges[1]}, {count}")

