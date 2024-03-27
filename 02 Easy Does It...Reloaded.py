################################################################################
# Name:  Brandon Fortes
# Date:  October 2, 2023
# Description:  A program that will give the average of two test scores given by the user... but with epic functions this time
################################################################################

name = ""
scores = 0

# A function that prompts the user for a name and returns it to the
# calling statement.
def askName():
    return input("Please enter your name: ")

# A function that prompts the user for a score and returns them to the
# calling statement. 
def askScores():
    return input("Enter your score: ")


# A function that receives a touple of numbers and returns the average of those
# numbers to the calling statement.
def average(num):      
    sum = 0;
    for i in num:
        sum += float(i)
    return sum / len(num)

# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def displayAverage(name, avg):
    print(f"Hi, {name}. Your average score is {avg}")

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
name = askName()

# prompt for two scores
scores = [askScores(), askScores()]

# calculate and display the average
displayAverage(name, average(scores))

