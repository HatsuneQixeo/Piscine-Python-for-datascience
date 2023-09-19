import give_bmi as bmi
import timeit
import sys

filename = "500_Person_Gender_Height_Weight_Index.csv"


class Person:
    def __init__(self, gender: str, height: int | float, weight: int | float,
                 index: int) \
            -> None:
        self.gender = gender
        self.height = height
        self.weight = weight
        self.index = index

    def __repr__(self) -> str:
        return f"{self.gender} \
[h:{self.height} w:{self.weight} i:{self.index}]"

    def get_height(self) -> int | float:
        return self.height / 100

    def get_weight(self) -> int | float:
        return self.weight


def read_file(filename: str) -> list[Person]:
    """Read the csv file and return a list of Person objects"""
    lst = list[Person]()
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            strlist = line.split(',')
            lst.append(Person(strlist[0], float(strlist[1]),
                              float(strlist[2]), int(strlist[3])))
    return lst


def main():
    lst_person = read_file(filename)
    lst_height = [person.get_height() for person in lst_person]
    lst_weight = [person.get_weight() for person in lst_person]

    start_time = timeit.default_timer()
    lst_bmi = bmi.give_bmi(lst_height, lst_weight)
    print(f"{(timeit.default_timer() - start_time) * 1000:f}", file=sys.stderr)

    start_time = timeit.default_timer()
    lst_limit = bmi.apply_limit(lst_bmi, 26)
    print(f"{(timeit.default_timer() - start_time) * 1000:f}", file=sys.stderr)

    print(lst_bmi)
    print(lst_limit)


if __name__ == "__main__":
    main()
