from dataclasses import dataclass

extension = ".csv"


@dataclass
class Student:
    student_id: int
    last_name: str
    first_name: str
    student_major: str
    disciplinary: str = ""
    gpa: str = ""
    graduation_date: str = ""



students = []
import csv

# Open file
with open('StudentsMajorsList-3.csv') as file_obj:

    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv
    # file using reader object
    for row in reader_obj:
        if row[-1] == "":
            row[-1] = "N"
        if row[-1] != "Y" and row[-1] != "N":
            row.append('N')
        student = Student(*row)
        students.append(student)


def partOne():
    """
    The items should
    be sorted alphabetically by student last name. Each row should contain student ID,
    major, first name, last name, GPA, graduation date and indicate if disciplinary action was
    taken. The student attributes must appear in this order in each row
    """
    lastname2student = dict()
    lastname2student_sorted = dict()
    for student in students:
        lastname2student[student.last_name] = student

    for entry in sorted(lastname2student.keys()):
        studentInfo = lastname2student[entry]
        lastname2student_sorted[studentInfo.last_name] = studentInfo

    print(lastname2student_sorted)

partOne()
