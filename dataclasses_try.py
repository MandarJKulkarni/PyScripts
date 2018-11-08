from dataclasses import dataclass


class OldStyleStudentInfo:
    roll_no = 0
    name = ''
    subjects = []

    def __init__(self, roll_no, name, subjects):
        self.roll_no = roll_no
        self.name = name
        self.subjects = subjects


@dataclass(order=True, unsafe_hash=True)
class StudentInfo:
    roll_no: int
    name: str
    subjects: list

@dataclass(frozen=True)
class Marks:
    maths: int
    english: int
    science: int
    hindi: int
