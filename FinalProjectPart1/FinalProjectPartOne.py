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

    def has_graduated(self) -> bool:
        """
        Has the student graduated yet? Cross-checks between the given date and today's date.
        """
        month, day, year = self.graduation_date.split("/")
        grad_date = datetime(int(year), int(month), int(day))
        current_date = datetime.today()
        return grad_date <= current_date


# endregion

### Beginning of student input/parsing ###
# region
ext = ".csv"
allRegisteredStudents = []

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

# Now we need to register the GPAs.
with open(f'GPAList-1{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        studentId, gpa = row
        studentEntry = id2student.get(studentId)
        if studentEntry:
            studentEntry.gpa = gpa


# endregion

### Beginning of CSV Output functions ###
# region
def generate_full_roster():
    """
    The items should be sorted alphabetically by student last name.
    The student attributes must appear in this order in each row:
        Student ID, major, first name, last name, GPA, graduation date, disciplinary action taken
    """
    lastname2student = dict()
    for student in allRegisteredStudents:
        lastname2student[student.last_name] = student

    csvFilename = f"FullRoster{ext}"
    csvFileOut = open(csvFilename, 'w')
    csvwriter = csv.writer(csvFileOut)

    # Write header
    csvwriter.writerow([
        "Student ID", "Major", "First Name", "Last Name", "GPA", "Graduation Date", "Disciplinary Action Taken"
    ])

    for lastName in sorted(lastname2student.keys()):
        studentInfo = lastname2student[lastName]
        studentId = studentInfo.student_id
        studentMajor = studentInfo.student_major
        firstName = studentInfo.first_name
        studentGpa = studentInfo.gpa
        gradDate = studentInfo.graduation_date
        dpAction = studentInfo.disciplinary
        csvwriter.writerow([studentId, studentMajor, firstName, lastName, studentGpa, gradDate, dpAction])

    csvFileOut.close()


def generate_major_stats():
    """
    Generates a csv file for each major (spaces truncated) with the respective students with that major.
    Contains student id, last name, first name, graduation date, disciplinary action indication.
    Entries sorted via Student ID.
    """
    allMajors = dict()

    # Now we will register students' majors.
    for student in allRegisteredStudents:
        # Check to see if the major key already exists. If not, create it.
        if not allMajors.get(student.student_major):
            allMajors[student.student_major] = [student]
        else:
            allMajors[student.student_major].append(student)

    # Now we will begin writing the CSV files:
    for majorName, majorStudents in allMajors.items():
        # Open up a new file for writing.
        csvFilename = f"{majorName.replace(' ', '')}{ext}"
        csvFileOut = open(csvFilename, 'w')
        csvwriter = csv.writer(csvFileOut)
        # Write header
        csvwriter.writerow(["Student ID", "Last Name", "First Name", "Graduation Date", "Disciplinary Action Taken"])

        # Sort all entries by ID.
        for studentId in sorted(id2student.keys()):
            studentInfo = id2student[studentId]
            lastName = studentInfo.last_name
            firstName = studentInfo.first_name
            gradDate = studentInfo.graduation_date
            dpAction = studentInfo.disciplinary
            csvwriter.writerow([studentId, lastName, firstName, gradDate, dpAction])

        csvFileOut.close()


def generate_scholarship_candidates():
    """
    Generates CSV file of all eligible students with GPAs > 3.8 and have not graduated or have had disciplinary action.
    Contains Student ID, last name, first name, major, and GPA.
    Sorted by highest GPA to lowest GPA.
    """
    # Open up a new file for writing.
    csvFilename = f"ScholarshipCandidates{ext}"
    csvFileOut = open(csvFilename, 'w')
    csvwriter = csv.writer(csvFileOut)
    # Write header
    csvwriter.writerow(["Student ID", "Last Name", "First Name", "Major", "GPA"])

    gpa2validStudents = dict()
    for student in allRegisteredStudents:
        if not float(student.gpa) > 3.8 and (student.has_graduated() or student.disciplinary == "Y"):
            continue
        # Just in case there is 2+ students with the same GPA,
        # we will set the value as a list of Student objects.
        # See if we've registered a key already:
        if not gpa2validStudents.get(student.gpa):
            gpa2validStudents[student.gpa] = [student]
        else:
            gpa2validStudents[student.gpa].append(student)

    # We have to reverse in order to get descending order
    for studentGpa in sorted(gpa2validStudents.keys(), reverse = True):
        studentsWithGpa = gpa2validStudents[studentGpa]
        for student in studentsWithGpa:
            studentInfo = student
            lastName = studentInfo.last_name
            firstName = studentInfo.first_name
            studentMajor = studentInfo.student_major
            studentId = studentInfo.student_id
            csvwriter.writerow([studentId, lastName, firstName, studentMajor, studentGpa])

    csvFileOut.close()


def generate_disciplined_students():
    """
    Generates a CSV file with students that have been disciplined.
    Contains the student ID, last name, first name, and graduation date.
    Sorted by graduation date, from oldest to most recent.
    """
    # Open up a new file for writing.
    csvFilename = f"DisciplinedStudents{ext}"
    csvFileOut = open(csvFilename, 'w')
    csvwriter = csv.writer(csvFileOut)
    # Write header
    csvwriter.writerow(["Student ID", "Last Name", "First Name", "Graduation Date"])

    gradDate2Students = dict()
    for student in allRegisteredStudents:
        if not student.disciplinary == "Y":
            continue
        # Just in case there is 2+ students with the same grad date,
        # we will set the value as a list of Student objects.
        # See if we've registered a key already:
        if not gradDate2Students.get(student.graduation_date):
            gradDate2Students[student.graduation_date] = [student]
        else:
            gradDate2Students[student.graduation_date].append(student)

    for gradDate in sorted(gradDate2Students.keys()):
        studentsWithGradDate = gradDate2Students[gradDate]
        for student in studentsWithGradDate:
            studentInfo = student
            studentId = studentInfo.student_id
            lastName = studentInfo.last_name
            firstName = studentInfo.first_name
            csvwriter.writerow([studentId, lastName, firstName, gradDate])
    csvFileOut.close()


# endregion

### Driver Code ###
if __name__ == "__main__":
    # Part 1
    generate_full_roster()
    # Part 2
    generate_major_stats()
    # Part 3
    generate_scholarship_candidates()
    # Part 4
    generate_disciplined_students()
