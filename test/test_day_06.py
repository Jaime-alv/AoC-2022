
import unittest

from day_06.day_06 import Day6


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
