################################################################################
# Name:  Brandon Fortes
# Date:  September 22, 2023
# Description:  A program that will give the average of two test scores given by the user
################################################################################

# Takes any number of numerical values and returns their average
def average(*num):      
    avg = 0;
    for i in num:
        avg += float(i)
    return avg / len(num)

# main process
# a statemant that prompts the user for their name
name = input("Please enter your name: ")

# statements that prompts the user for two test scores
scoreOne = input(f"Hi {name}. What did you score on your first test? ")
scoreTwo = input("What did you score on your second test? ")

# display the final output
print(f"The average of {scoreOne} and {scoreTwo} is {average(scoreOne, scoreTwo)}")



