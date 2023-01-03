
import unittest

from day_08 import day_08 as d


class TestDay08(unittest.TestCase):
    example: list[int] = [
        30373,
        25512,
        65332,
        33549,
        35390,
    ]

    def test_transform(self):
        raw: list[str] = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390",
        ]
        self.assertListEqual(d.transform_into_int(raw), self.example)
