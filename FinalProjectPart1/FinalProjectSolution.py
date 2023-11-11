import csv
from datetime import datetime


### Student class generation ###
# region
class Student:
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
        month, day, year = self.graduation_date.split("/")
        grad_date = datetime(int(year), int(month), int(day))
        current_date = datetime.today()
        return grad_date <= current_date


allRegisteredStudents = []
# endregion

### Beginning of student input/parsing ###
# region
ext = ".csv"

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
    List per major, i.e. ComputerInformationSystemsStudents.csv -- there should be a file for
    each major and the major needs to be in the file name, the spaces in the major name
    should be eliminated for the file name. Each row of the file should contain student ID,
    last name, first name, graduation date, and indicate if disciplinary action was taken. The
    students should be sorted by their student ID.
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
        csvFilename = f"{majorName.strip()}{ext}"
        csvFileOut = open(csvFilename, 'w')
        csvwriter = csv.writer(csvFileOut)
        # Write header
        csvwriter.writerow(["Student ID", "Last Name", "First Name", "Graduation Date", "Disciplinary Action Taken"])

        # Sort all entries by ID.
        for studentId in sorted(id2student.keys()):
            studentInfo = id2student[studentId]
            lName = studentInfo.last_name
            fName = studentInfo.first_name
            gradDate = studentInfo.graduation_date
            dpAction = studentInfo.disciplinary
            csvwriter.writerow([studentId, lName, fName, gradDate, dpAction])

        csvFileOut.close()


def generate_scholarship_candidates():
    """
    c. ScholarshipCandidates.csv – should contain a list of all eligible students with GPAs > 3.8.
    Students who have graduated or have had disciplinary action taken are not eligible. Each
    row should contain: student ID, last name, first name, major, and GPA. The students
    must appear in the order of GPA from highest to lowest
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
        if not gpa2validStudents.get(student.gpa):
            gpa2validStudents[student.gpa] = [student]
        else:
            gpa2validStudents[student.gpa].append(student)

    # We have to reverse in order to get descending order
    for studentGpa in sorted(gpa2validStudents.keys(), reverse = True):
        studentsWithGpa = gpa2validStudents[studentGpa]
        for student in studentsWithGpa:
            studentInfo = student
            lName = studentInfo.last_name
            fName = studentInfo.first_name
            studentMajor = studentInfo.student_major
            studentId = studentInfo.student_id
            csvwriter.writerow([studentId, lName, fName, studentMajor, studentGpa])
    csvFileOut.close()


def generate_disciplined_students():
    """
    DisciplinedStudents.csv –all students that have been disciplined. Each row should
    contain: student ID, last name, first name, and graduation date. The students must
    appear in the order of graduation date from oldest to most recent
    """
    pass

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
