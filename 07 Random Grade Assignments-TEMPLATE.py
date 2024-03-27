####################################################################
# author: Brandon Fortes
# date: November 8, 2023
# desc: This program generates a list of random number grades, calculates its associated 
# letter grades and the average grade, and then prints them out
###################################################################

import random

# constants defined to limit the scope of the randomly generated grades.
LOWEST_GRADE = 65
HIGHEST_GRADE = 100

# A function that prompts the user for the number of students in the
# class and returns that value to the calling statement.
def getNumStudents():
    return int(input("How many students are in this imaginary class? "))

# A function that receives the number of students as an argument, and
# creates a list of random integers of that size. The complete list is
# returned to the calling statement.
def generateGrades(size):
    gradeList = []
    i = 0
    while(i < size):
        gradeList.append(random.randint(LOWEST_GRADE, HIGHEST_GRADE))
        i += 1
    return gradeList

# A function that receives a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.
def getLetterGrade(grade):
    if (grade >= 90):
        return "A"
    elif (grade >= 80):
        return "B"
    elif (grade >= 70):
        return "C"
    elif (grade >= 60):
        return "D"
    else:
        return "F"

# A function that receives a list of values and a print end condition, and prints them in order.
def printList(list, endStr):
    for val in list:
        print(str(val), end = endStr)

# A function that recieves a list of numerical values (corresponding to
# the numerical grades), and creates a list of corresponding letter
# grades. This list of letter grades is then returned to the calling
# statement.
def listLetterGrades(numList):
    letterList = []
    for num in numList:
        letterList.append(getLetterGrade(num))
    return letterList

# A function that recieves a list of numerical values, and returns the
# mean/average of that list.
def getListAverage(numList):
    sum = 0
    for num in numList:
        sum += num
    return sum / len(numList)

############################# main ############################

# using functions defined above, get the class size, numerical grade
# list, and letter grade list.
numOfStudents = getNumStudents()
numberGrades = generateGrades(numOfStudents)
letterGrades = listLetterGrades(numberGrades)

# Print out both numerical and letter grades as well as the average.
print("Numerical Grades: ")
printList(numberGrades, "   ")
print("\nLetter Grades: ")
printList(letterGrades, "    ")
print(f"\nThe average grade for the class is {getListAverage(numberGrades)}")