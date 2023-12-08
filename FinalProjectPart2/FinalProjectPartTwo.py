"""
Erica Miller
2031854


A Program that manages student records at a university
"""

import csv
from datetime import datetime


### Student class generation ###
# region
class Student:
    """
    Contains the records of a single Student, including:
    full name, student id, major, gpa, grad date, if they graduated yet, and disciplinary record.
    """

    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.last_name} {self.gpa}"

    def __repr__(self):
        return f"{self.student_id} {self.first_name} {self.last_name} {self.gpa}"

    def __init__(self,
                 student_id: int,
                 last_name: str, first_name: str,
                 student_major: str, disciplinary: str = "",
                 gpa: str = "", graduation_date: str = ""):
        self.student_id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.student_major = student_major
        self.disciplinary = disciplinary
        self.gpa = gpa
        self.graduation_date = graduation_date

    def hasGraduated(self) -> bool:
        """
        Has the student graduated yet? Cross-checks between the given date and today's date.
        """
        if not self.graduation_date:
            return True
        month, day, year = self.graduation_date.split("/")
        grad_date = datetime(int(year), int(month), int(day))
        current_date = datetime.today()
        return grad_date <= current_date

    def hasDisciplinaryAction(self) -> bool:
        """
        :return: Boolean equivalent of disciplinary record
        """
        return self.disciplinary == "Y"

    def is_valid(self) -> bool:
        return not (self.has_graduated() and self.has_disciplinary_action())


    def isGpaApproximate(self, targetGpa:float, margin:float) -> bool:
        studentGpa = float(self.gpa)

        deltaGpa = abs(round(studentGpa - targetGpa, 2))

        # Anything >0 is out of bounds
        gpaBounds = [
            round(deltaGpa - margin, 2),  # Lower bound of margin
            round(deltaGpa, 2)  # Upper bound of margin
        ]

        # print(f"gpaBounds = {gpaBounds} | student {studentGpa} | target {targetGpa} | margin {margin}")
        return (gpaBounds[0] <= 0) or (gpaBounds[1] <= margin) or studentGpa == targetGpa


# endregion

# Null student is a default dummy student that is temporarily assigned as the "closest" student,
# but immediately gets replaced by the first registered student.
nullStudent = Student(0, "last", "first", "major", "disciplinary", "99.0", "9/9/9999")


### Beginning of student input/parsing ###
# region
ext = ".csv"
allRegisteredStudents = []
allMajors = set()

# Open our file w/ all our students and parse data into a Student object
with open(f'StudentsMajorsList-3{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    # Our disciplinary entries are half-baked. For ones who don't have any, create an entry with "N"
    # So that the sizes of our rows are balanced.
    for row in csvReader:
        if row[-1] == "":
            row[-1] = "N"
        if row[-1] != "Y" and row[-1] != "N":
            row.append('N')
        student = Student(*row)
        allMajors.add(student.student_major.lower())
        # We can ignore students who have disciplinary action on record
        if not student.hasDisciplinaryAction():
            allRegisteredStudents.append(student)


# We're not done registering our students just yet -- we need to open up two more CSV files
# that hold graduation dates & GPA.

# Student.id : Student
id2student = dict()

for student in allRegisteredStudents:
    id2student[student.student_id] = student

# First, we need to register the graduation dates for the students.
with open(f'GraduationDatesList-1{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        studentId, gradDate = row
        studentEntry = id2student.get(studentId)
        if studentEntry:
            studentEntry.graduation_date = gradDate
            if studentEntry.hasGraduated():
                # Kill student if they have graduated
                allRegisteredStudents.remove(studentEntry)
                del id2student[studentId]

# Now we need to register the GPAs.
with open(f'GPAList-1{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        studentId, gpa = row
        studentEntry = id2student.get(studentId)
        if studentEntry:
            studentEntry.gpa = gpa


def searchForStudent(userInput):
    userInput = userInput.lower()
    userMajor = ""  # todo: write code for unknown major or never registered
    userGpa = 0.0  # todo: write code for gpa never registered
    registeredMajor = False
    registeredGpa = False

    for major in allMajors:
        if major in userInput:
            if registeredMajor:
                # Major registered twice
                return print("No such student")
            userMajor = major
            registeredMajor = True

    for entry in userInput.split(" "):
        entryVal = entry.replace(".", "")
        if entryVal.isnumeric():
            if registeredGpa:
                # Gpa registered twice
                return print("No such student")
            userGpa = float(entry)
            registeredGpa = True

    if not registeredGpa or not registeredMajor:
        return print("No such student")

    nullStudent.student_major = userMajor

    # Search for our student(s)
    validStudents = list()
    possibleStudents = list()
    closestStudent = nullStudent
    for student in allRegisteredStudents:
        if student.student_major.lower() == userMajor:
            if student.isGpaApproximate(userGpa, 0.25):
                # print(f"--- Student gpa {student.gpa} is close enough to {userGpa}")
                if student.isGpaApproximate(userGpa, 0.1):
                    validStudents.append(student)
                else:
                    possibleStudents.append(student)
            else:
                # Get student that has closet GPA to what was requested
                # Lower delta = closer to user input
                deltaStudentGpa = abs(float(student.gpa) - userGpa)
                deltaClosestGpa = abs(float(closestStudent.gpa) - userGpa)
                closestStudent = student if deltaStudentGpa < deltaClosestGpa else closestStudent

    if validStudents:
        print(f"Valid students found {validStudents} from {userMajor} | {userGpa}")
        if possibleStudents:
            print(f"You may also consider {possibleStudents} from {userMajor} | {userGpa}")
    else:
        print(f"Closest match found: {closestStudent} from {userMajor} | {userGpa}")

### Driver Code ###
if __name__ == "__main__":
    # Ask for major and GPA
    # userInput = input().lower()
    possibleGpas = [round(float(x / 10), 2) for x in range(0, 41)]
    for major in allMajors:
        for gpa in possibleGpas:
            searchForStudent(f"{major} {gpa}")



