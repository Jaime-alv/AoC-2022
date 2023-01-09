
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

    def test_scenic_factor_by_list(self):
        trees: list[int] = [3, 0, 3, 7, 3]
        self.assertEqual(self.base_day.count_elements_in_list(3, trees), 1)
        self.assertEqual(self.base_day.count_elements_in_list(4, trees), 4)
        self.assertEqual(self.base_day.count_elements_in_list(8, trees), 5)
        self.assertEqual(self.base_day.count_elements_in_list(5, [3, 5, 3]), 2)

    def test_reverse_list(self):
        trees: list[int] = [3, 0, 3, 7, 3]
        trees.reverse()
        self.assertListEqual(trees, [3, 7, 3, 0, 3])

    def test_iterate_part_2(self):
        self.assertEqual(self.base_day.iterate_data_for_scenic_view(), 8)

    def test_tuple_conform(self):
        tree_house: int = 5
        top: list[int] = [3, 5, 3]
        down: list[int] = [3]
        left: list[int] = [3, 3]
        right: list[int] = [4, 9]
        self.assertEqual(self.base_day.conform_scenic_score(
            tree_house, top, down, left, right), 8)

    def test_example(self):
        tree_house: int = 5
        top: list[int] = [3, 5, 3]
        down: list[int] = [3]
        left: list[int] = [3, 3]
        right: list[int] = [4, 9]
        self.assertEqual(self.base_day.count_elements_in_list(tree_house, top), 2)
        self.assertEqual(self.base_day.count_elements_in_list(tree_house, down), 1)
        self.assertEqual(self.base_day.count_elements_in_list(tree_house, left), 2)
        self.assertEqual(self.base_day.count_elements_in_list(tree_house, right), 2)
