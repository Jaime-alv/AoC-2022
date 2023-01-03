from pathlib import Path


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


if __name__ == '__main__':
    input_file: Path = Path("./day_01/input.txt")
    print(process_part_1(load_file(input_file)))
    print(process_part_2(load_file(input_file)))
