from dataclasses import dataclass
import csv

ext = ".csv"


@dataclass
class Student:
    student_id: int
    last_name: str
    first_name: str
    student_major: str
    disciplinary: str = ""
    gpa: str = ""
    graduation_date: str = ""


allRegisteredStudents = []

# Open our file w/ all our students and parse data into a Student object
with open(f'StudentsMajorsList-3{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    # Our disciplinary entries are half-baked. For ones who don't have any, create a entry with "N"
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
        studentId, gdate = row
        studentEntry = id2student.get(studentId)
        if studentEntry:
            studentEntry.graduation_date = gdate

# Now we need to register the GPAs.
with open(f'GPAList-1{ext}') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        studentId, gpa = row
        studentEntry = id2student.get(studentId)
        if studentEntry:
            studentEntry.gpa = gpa


def partOne():
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

def partTwo():
    """
    List per major, i.e ComputerInformationSystemsStudents.csv -- there should be a file for
    each major and the major needs to be in the file name, the spaces in the major name
    should be eliminated for the file name. Each row of the file should contain student ID,
    last name, first name, graduation date, and indicate if disciplinary action was taken. The
    students should be sorted by their student ID.
    """
    pass
    
def partThree():
    """
    c. ScholarshipCandidates.csv – should contain a list of all eligible students with GPAs > 3.8.
    Students who have graduated or have had disciplinary action taken are not eligible. Each
    row should contain: student ID, last name, first name, major, and GPA. The students
    must appear in the order of GPA from highest to lowest
    """
    pass


partOne()
partTwo()
