from pathlib import Path
import unittest


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


def iterate_list(data: list[str]) -> list[int]:
    result: list[int] = []
    tmp: list[int] = []
    for element in data:
        if element != '':
            tmp.append(int(element))
        else:
            result.append(sum_splits(tmp))
            tmp.clear()

    return sorted(result)


def find_max(data: list[int]) -> int:
    return max(data)


def sum_splits(data: list[int]) -> int:
    return sum(data)


def process_part_1(data: list[str]) -> int:
    return find_max(iterate_list(data))


def process_part_2(data: list[str]) -> int:
    return sum_splits(sorted(iterate_list(data), reverse=True)[:3])


class TestDay1(unittest.TestCase):
    example = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
        ""
    ]

    def test_splits(self):
        self.assertEqual(sum_splits([1, 2, 3]), 6)

    def test_iterate(self):
        self.assertListEqual(iterate_list(self.example),
                             sorted([6000, 4000, 11000, 24000, 10000]))

    def test_max(self):
        self.assertEqual(find_max([6000, 4000, 11000, 24000, 10000]), 24000)

    def test_part1(self):
        self.assertEqual(process_part_1(self.example), 24000)

    def test_part2(self):
        self.assertEqual(process_part_2(self.example), 45000)


if __name__ == '__main__':
    input_file: Path = Path("./day1/input.txt")
    print(process_part_1(load_file(input_file)))
    print(process_part_2(load_file(input_file)))
    unittest.main()
