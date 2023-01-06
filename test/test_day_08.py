
import unittest

from day_08.day_08 import ForestMatrix


class TestDay08(unittest.TestCase):
    example: list[int] = [
        30373,
        25512,
        65332,
        33549,
        35390,
    ]

    raw: list[str] = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    base_day: ForestMatrix = ForestMatrix(raw)

    def test_conforming(self):
        self.assertTupleEqual(
            self.base_day.conform_column_list(0, 1), ([3], [6, 3, 3]))
        self.assertTupleEqual(
            self.base_day.conform_column_list(0, 0), ([], [2, 6, 3, 3]))
        self.assertTupleEqual(
            self.base_day.conform_column_list(2, 4), ([3, 5, 3, 5], []))
        self.assertTupleEqual(
            self.base_day.conform_column_list(3, 3), ([7, 1, 3], [9]))
        self.assertTupleEqual(
            self.base_day.conform_column_list(4, 3), ([3, 2, 2], [0]))

    def test_row_list(self):
        line: str = "30373"
        self.assertTupleEqual(self.base_day.conform_row_list(
            line, 2), ([3, 0], [7, 3]))
        self.assertTupleEqual(self.base_day.conform_row_list(
            line, 0), ([], [0, 3, 7, 3]))
        self.assertTupleEqual(self.base_day.conform_row_list(
            line, 1), ([3], [3, 7, 3]))
        self.assertTupleEqual(self.base_day.conform_row_list(
            line, 5), ([3, 0, 3, 7, 3], []))

    def test_parsing(self):
        self.assertEqual(self.base_day.parse_line_notice(2),
                         "Parsing line: (3/5)")

    def test_smaller(self):
        line: list[int] = [1, 2, 3, 4,]
        tree: int = 6
        self.assertTrue(self.base_day.check_all_smaller(tree, line))
        self.assertFalse(self.base_day.check_all_smaller(4, line))

    def test_iterate_data(self):
        new_day: ForestMatrix = ForestMatrix(self.raw)
        new_day.iterate_data()
        self.assertEqual(new_day.counter, 21)
