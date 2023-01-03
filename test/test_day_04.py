
import unittest

from day_04 import day_04 as d


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
        self.assertEqual(d.split_pairs('2-4,6-8'), ((2, 4), (6, 8)))
        self.assertEqual(d.split_pairs('2-6,4-8'), ((2, 6), (4, 8)))
        self.assertEqual(d.split_pairs('5-7,7-9'), ((5, 7), (7, 9)))

    def test_conversion(self):
        self.assertEqual(d.convert_to_list((2, 4)), [2, 3, 4])
        self.assertEqual(d.convert_to_list((5, 7)), [5, 6, 7])
        self.assertEqual(d.convert_to_list((7, 7)), [7])

    def test_map(self):
        self.assertTrue(d.map_through(
            d.convert_to_list((2, 4)), d.convert_to_list((2, 5))))
        self.assertFalse(d.map_through(
            d.convert_to_list((2, 4)), d.convert_to_list((6, 8))))
        self.assertTrue(d.map_through(
            d.convert_to_list((2, 4)), d.convert_to_list((1, 8))))
        self.assertTrue(d.map_through(
            d.convert_to_list((1, 8)), d.convert_to_list((1, 8))))
        self.assertFalse(d.map_through(
            d.convert_to_list((1, 8)), d.convert_to_list((3, 4))))

    def test_double_map(self):
        self.assertFalse(d.contain(((2, 4), (6, 8))))
        self.assertTrue(d.contain(((2, 4), (2, 8))))
        self.assertTrue(d.contain(((1, 7), (3, 4))))
        self.assertFalse(d.contain(((2, 4), (6, 8))))

    def test_algorithm(self):
        self.assertEqual(d.counter(self.example), 2)

    def test_one_by_one(self):
        self.assertFalse(d.contain(((2, 4), (6, 8))))
        self.assertFalse(d.contain(((2, 3), (4, 5))))
        self.assertFalse(d.contain(((5, 7), (7, 9))))
        self.assertTrue(d.contain(((2, 8), (3, 7))))
        self.assertTrue(d.contain(((6, 6), (4, 6))))
        self.assertFalse(d.contain(((2, 6), (4, 8))))

    def test_loop_counter(self):
        self.assertEqual(d.loop_counter(self.example), 4)

    def test_overlap(self):
        self.assertEqual(d.process_tuple(((5, 7), (7, 9))), [7])
        self.assertEqual(d.process_tuple(((2, 8), (3, 7))), [3, 4, 5, 6, 7])
        self.assertEqual(d.process_tuple(((6, 7), (4, 6))), [6])
        self.assertEqual(d.process_tuple(((2, 6), (4, 8))), [4, 5, 6])
