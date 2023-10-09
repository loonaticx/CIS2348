# Erica Miller 2031854
# Write a basic program that performs simple file and mathematical
# operations.

import datetime

monthList = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Easy way to generate number count w/ the months
monthVals = list(range(1, len(monthList) + 1))

# { "month": monthId }
monthDict = dict(zip(monthList, monthVals))

currentDate = datetime.datetime.now()


## Part A
def runPartA():

    def getDate():
        return input("Enter a date: ")

    inputDate = 1
    while inputDate != "-1":
        # Prompt user for input
        inputDate = getDate()

        # If we don't have any spaces then let's get out of here.
        if inputDate.find(" ") == -1:
            continue

        # We'll use the find method to parse the input.
        # monthName should start from the beginning and end right before the space.
        monthName: str = inputDate[:inputDate.find(" ", inputDate.find(" "))]
        # Cull out the month name + " " since we don't care about it anymore.
        inputDate = inputDate[len(monthName) + 1:]

        # dayNum is now at the beginning and should end right before another space.
        dayNum = inputDate[:inputDate.find(" ", inputDate.find(' '))]
        # First clause is important to avoid edge case like "foo "
        if dayNum.find(",") == -1 or dayNum[-1] != ",":
            continue

        # Kill da comma
        dayNum = dayNum[:-1]
        if not dayNum:
            continue

        # Get the year number now.
        # We add one more since we also need to consider the comma we just killed.
        yearNum = inputDate[len(dayNum) + 2:]

        # Year must be exactly 4 digits, if not, then it isn't a proper value.
        if len(yearNum) != 4:
            continue

        # Check for a valid input month (case-sensitive)
        monthNum = monthDict.get(monthName, 0)
        if not monthNum:
            continue

        # Finally, let's parse this into a datetime object
        # Want to make a datetime object here, but make sure we don't run into any invalid input.
        try:
            userDate = datetime.datetime(year = int(yearNum), month = monthNum, day = int(dayNum))
        except ValueError:
            continue

        # Ignore any dates that are later than the current date
        if userDate > currentDate:
            continue
        print(f"{monthNum}/{dayNum}/{yearNum}")


## Part B
def runPartB():
    inputFile = open("inputDates.txt", "r")

    for line in inputFile.readlines():
        # Kill the CRLF
        inputDate = line.rstrip("\n")

        # If we don't have any spaces then let's get out of here.
        if inputDate.find(" ") == -1:
            # A -1 entry terminates our search.
            if inputDate == "-1":
                break
            continue

        # We'll use the find method to parse the input.
        # monthName should start from the beginning and end right before the space.
        monthName: str = inputDate[:inputDate.find(" ", inputDate.find(" "))]
        # Cull out the month name + " " since we don't care about it anymore.
        inputDate = inputDate[len(monthName) + 1:]

        # dayNum is now at the beginning and should end right before another space.
        dayNum = inputDate[:inputDate.find(" ", inputDate.find(' '))]
        # First clause is important to avoid edge case like "foo "
        if dayNum.find(",") == -1 or dayNum[-1] != ",":
            continue

        # Kill da comma
        dayNum = dayNum[:-1]
        if not dayNum:
            continue

        # Get the year number now.
        # We add one more since we also need to consider the comma we just killed.
        yearNum = inputDate[len(dayNum) + 2:]

        # Year must be exactly 4 digits, if not, then it isn't a proper value.
        if len(yearNum) != 4:
            continue

        # Check for a valid input month (case-sensitive)
        monthNum = monthDict.get(monthName, 0)
        if not monthNum:
            continue

        # Finally, let's parse this into a datetime object
        # Want to make a datetime object here, but make sure we don't run into any invalid input.
        try:
            userDate = datetime.datetime(year = int(yearNum), month = monthNum, day = int(dayNum))
        except ValueError:
            continue

        # Ignore any dates that are later than the current date
        if userDate > currentDate:
            continue
        print(f"{monthNum}/{dayNum}/{yearNum}")

## Part C
def runPartC():
    inputFile = open("inputDates.txt", "r")
    outputFile = open("parsedDates.txt", "w")
    validDates = list()

    for line in inputFile.readlines():
        # Kill the CRLF
        inputDate = line.rstrip("\n")

        # If we don't have any spaces then let's get out of here.
        if inputDate.find(" ") == -1:
            # A -1 entry terminates our search.
            if inputDate == "-1":
                break
            continue

        # We'll use the find method to parse the input.
        # monthName should start from the beginning and end right before the space.
        monthName: str = inputDate[:inputDate.find(" ", inputDate.find(" "))]
        # Cull out the month name + " " since we don't care about it anymore.
        inputDate = inputDate[len(monthName) + 1:]

        # dayNum is now at the beginning and should end right before another space.
        dayNum = inputDate[:inputDate.find(" ", inputDate.find(' '))]
        # First clause is important to avoid edge case like "foo "
        if dayNum.find(",") == -1 or dayNum[-1] != ",":
            continue

        # Kill da comma
        dayNum = dayNum[:-1]
        if not dayNum:
            continue

        # Get the year number now.
        # We add one more since we also need to consider the comma we just killed.
        yearNum = inputDate[len(dayNum) + 2:]

        # Year must be exactly 4 digits, if not, then it isn't a proper value.
        if len(yearNum) != 4:
            continue

        # Check for a valid input month (case-sensitive)
        monthNum = monthDict.get(monthName, 0)
        if not monthNum:
            continue

        # Finally, let's parse this into a datetime object
        # Want to make a datetime object here, but make sure we don't run into any invalid input.
        try:
            userDate = datetime.datetime(year = int(yearNum), month = monthNum, day = int(dayNum))
        except ValueError:
            continue

        # Ignore any dates that are later than the current date
        if userDate > currentDate:
            continue

        validDates.append(f"{monthNum}/{dayNum}/{yearNum}")

    for date in validDates:
        outputFile.write(f"{date}\n")
    outputFile.close()


if __name__ == "__main__":
    runPartC()
