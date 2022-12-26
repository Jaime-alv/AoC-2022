from collections import Counter
import pathlib
import unittest


def load_file(file: pathlib.Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class Day6:
    def __init__(self, data: str) -> None:
        self.data = data

    def iterate_str(self, plus: int) -> int | None:
        for index in range(len(self.data)):
            tmp = self.data[index: index + plus]
            if self.count_chars(tmp):
                return index + plus

    def count_chars(self, data: str) -> bool:
        counter = Counter(data)
        return all(map(lambda x: x == 1, counter.values()))


class Day6Test(unittest.TestCase):
    example_0: str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    example_1: str = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    example_2: str = "nppdvjthqldpwncqszvftbrmjlhg"
    example_3: str = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    example_4: str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    def setUp(self) -> None:
        self.day6: Day6 = Day6(self.example_0)
        return super().setUp()

    def test_counter(self):
        self.assertFalse(self.day6.count_chars("mjqj"))
        self.assertFalse(self.day6.count_chars("mqqj"))
        self.assertTrue(self.day6.count_chars("mjqz"))
        self.assertTrue(self.day6.count_chars("mjqr"))

    def test_iterate(self):
        self.assertEqual(self.day6.iterate_str(4), 7)
        self.assertEqual(Day6(self.example_1).iterate_str(4), 5)
        self.assertEqual(Day6(self.example_2).iterate_str(4), 6)
        self.assertEqual(Day6(self.example_3).iterate_str(4), 10)
        self.assertEqual(Day6(self.example_4).iterate_str(4), 11)


if __name__ == '__main__':
    input_file: pathlib.Path = pathlib.Path("./day6/input.txt")
    print(Day6(load_file(input_file)[0]).iterate_str(4))
    print(Day6(load_file(input_file)[0]).iterate_str(14))
    unittest.main(verbosity=2)
