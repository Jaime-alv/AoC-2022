from pathlib import Path


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class ForestMatrix:
    counter: int = 0

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def check_all_smaller(self, tree_house: int, trees: list[int]) -> bool:
        return all(map(lambda x: x < tree_house, trees))

    def parse_result(self, tautology: tuple[bool, bool, bool, bool]) -> None:
        if any(tautology):
            self.counter += 1

    def iterate_data(self):
        for index_row, v_row in enumerate(self.data):
            print(self.parse_line_notice(index_row))
            for i_column, v_column in enumerate((self.data[index_row])):
                top, down = self.conform_column_list(i_column, index_row)
                left, right = self.conform_row_list(v_row, i_column)
                tautology: tuple[bool, bool, bool, bool] = (
                    self.check_all_smaller(int(v_column), top),
                    self.check_all_smaller(int(v_column), down),
                    self.check_all_smaller(int(v_column), left),
                    self.check_all_smaller(int(v_column), right),
                )
                self.parse_result(tautology)

    def conform_column_list(self, index: int, div: int) -> tuple[list[int], list[int]]:
        tmp: list[int] = []
        for line in self.data:
            tmp.append(int(line[index]))
        return tmp[0:div], tmp[div + 1:]

    def conform_row_list(self, line: str, index: int) -> tuple[list[int], list[int]]:
        conversion: list[int] = [int(x) for x in line]
        return conversion[:index], conversion[index + 1:]

    def parse_line_notice(self, index: int) -> str:
        return f"Parsing line: ({index + 1}/{len(self.data)})"

    def part_one(self) -> str:
        self.iterate_data()
        return f"Result for part one is: {self.counter}"


if __name__ == '__main__':
    input_file = Path("./day_08/input.txt")

    forest = ForestMatrix(load_file(input_file))
    print(forest.part_one())
