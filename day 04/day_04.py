import pathlib
import unittest


def split_pairs(pair: str) -> tuple[tuple[int, int], tuple[int, int]]:
    hold: list[str] = pair.split(",")
    first: tuple[int, int] = form_tuple(hold[0])
    second: tuple[int, int] = form_tuple(hold[1])
    return first, second


def form_tuple(element: str) -> tuple[int, int]:
    return int(element.split("-")[0]), int(element.split("-")[1])


def convert_to_list(data: tuple[int, int]) -> list[int]:
    return list(range(data[0], data[1] + 1))


def contain(data: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    first: list[int] = convert_to_list(data[0])
    second: list[int] = convert_to_list(data[1])
    if map_through(first, second) or map_through(second, first):
        return True
    return False


def map_through(list1: list[int], list2: list[int]) -> bool:
    for number in list1:
        if number not in list2:
            return False
    return True


def counter(data: list[str]) -> int:
    result: int = 0
    for element in data:
        first, second = split_pairs(element)
        if contain((first, second)):
            result += 1
    return result


def load_file(file: pathlib.Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


def part1(file: pathlib.Path) -> int:
    return counter(load_file(file))


def overlap(list1: list[int], list2: list[int]) -> list[int]:
    return list(filter(lambda x: x in list2, list1))


def part2(file: pathlib.Path) -> int:
    data: list[str] = load_file(file)
    return loop_counter(data)


def process_tuple(data: tuple[tuple[int, int], tuple[int, int]]) -> list[int]:
    first: list[int] = convert_to_list(data[0])
    second: list[int] = convert_to_list(data[1])
    return overlap(first, second)


def loop_counter(data: list[str]) -> int:
    result: int = 0
    for element in data:
        first, second = split_pairs(element)
        buffer_list: list[int] = process_tuple((first, second))
        if len(buffer_list) > 0:
            result += 1
    return result


class Day4Test(unittest.TestCase):
    example = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    def test_split_pair(self):
        self.assertEqual(split_pairs('2-4,6-8'), ((2, 4), (6, 8)))
        self.assertEqual(split_pairs('2-6,4-8'), ((2, 6), (4, 8)))
        self.assertEqual(split_pairs('5-7,7-9'), ((5, 7), (7, 9)))

    def test_conversion(self):
        self.assertEqual(convert_to_list((2, 4)), [2, 3, 4])
        self.assertEqual(convert_to_list((5, 7)), [5, 6, 7])
        self.assertEqual(convert_to_list((7, 7)), [7])

    def test_map(self):
        self.assertTrue(map_through(
            convert_to_list((2, 4)), convert_to_list((2, 5))))
        self.assertFalse(map_through(
            convert_to_list((2, 4)), convert_to_list((6, 8))))
        self.assertTrue(map_through(
            convert_to_list((2, 4)), convert_to_list((1, 8))))
        self.assertTrue(map_through(
            convert_to_list((1, 8)), convert_to_list((1, 8))))
        self.assertFalse(map_through(
            convert_to_list((1, 8)), convert_to_list((3, 4))))

    def test_double_map(self):
        self.assertFalse(contain(((2, 4), (6, 8))))
        self.assertTrue(contain(((2, 4), (2, 8))))
        self.assertTrue(contain(((1, 7), (3, 4))))
        self.assertFalse(contain(((2, 4), (6, 8))))

    def test_algorithm(self):
        self.assertEqual(counter(self.example), 2)

    def test_one_by_one(self):
        self.assertFalse(contain(((2, 4), (6, 8))))
        self.assertFalse(contain(((2, 3), (4, 5))))
        self.assertFalse(contain(((5, 7), (7, 9))))
        self.assertTrue(contain(((2, 8), (3, 7))))
        self.assertTrue(contain(((6, 6), (4, 6))))
        self.assertFalse(contain(((2, 6), (4, 8))))

    def test_loop_counter(self):
        self.assertEqual(loop_counter(self.example), 4)

    def test_overlap(self):
        self.assertEqual(process_tuple(((5, 7), (7, 9))), [7])
        self.assertEqual(process_tuple(((2, 8), (3, 7))), [3, 4, 5, 6, 7])
        self.assertEqual(process_tuple(((6, 7), (4, 6))), [6])
        self.assertEqual(process_tuple(((2, 6), (4, 8))), [4, 5, 6])


if __name__ == '__main__':
    input_file = pathlib.Path("./day 04/input.txt")
    print(part1(input_file))
    print(part2(input_file))
    unittest.main()
