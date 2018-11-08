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


std1 = StudentInfo(14,'Vijay',['Maths','Science'])
std2 = StudentInfo(15,'Ajay',['Hindi','English'])

if std1 != std2:
    print('2 students are not equal')

#data classes are mutable by default
std1.roll_no=15
std1.name='Ajay'
std1.subjects = ['Hindi', 'English']

if std1 == std2:
    print('2 students are equal')

@dataclass(frozen=True)
class Marks:
    maths: int
    english: int
    science: int
    hindi: int
