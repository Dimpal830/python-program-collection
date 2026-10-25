"""Convert structured data into dictionaries."""

from collections import namedtuple
from dataclasses import dataclass, asdict


class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def to_dict(self):
        return vars(self)


@dataclass
class Book:
    title: str
    author: str
    pages: int


Point = namedtuple("Point", ["x", "y"])


def main():
    student = Student("Aastha", "25BCON2383", "CSE")
    book = Book("Atomic Habits", "James Clear", 320)
    point = Point(3, 7)

    print("Class      ->", student.to_dict())
    print("Dataclass  ->", asdict(book))
    print("Namedtuple ->", point._asdict())


if __name__ == "__main__":
    main()