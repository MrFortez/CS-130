##########################################################################################
# Name: Brandon Fortes
# Date: October 30, 2023
# Description: This program will compare the preformance of binary search and sequential search through a table with user given values
##########################################################################################

import math

# a function that asks the user for an integer value to represent the minimun value of the table, accounting for errors given if the value is not a positive integer
# -output: a user given integer value
def getMinOfTable(): 
    try:
        num = int(input("Minimum number of list items (>=0)? "))
    except:
        print(" *ERROR: Minimum must be >= 0!")
        return getMinOfTable()
    else:
        if (num < 0):
            print(" *ERROR: Minimum must be >= 0!")
            return getMinOfTable()
        return num
    
# a function that asks the user for an integer value to represent the maximum value of the table, accounting for errors given if the value is not a positive integer or is less than the minimun
# -input: the minimun value of the list
# -output: a user given integer value
def getMaxOfTable(minVal): 
    try:
        num = int(input(f"Maximum number of list items (>= min ({minVal}))? "))
    except:
        print(f" *ERROR: Maximum must be >= minimum ({minVal})! ")
        return getMaxOfTable(minVal)
    else:
        if (num < minVal):
            print(f" *ERROR: Maximum must be >= minimum ({minVal})! ")
            return getMaxOfTable(minVal)
        return num
    
# a function that asks the user for an integer value to represent the intervals of the table, accounting for errors given if the value is not an integer greater than or equal to 1
# -output: a user given integer value
def getIntervalOfTable(): 
    try:
        num = int(input("The interval between each row of the table (>= 1)? "))
    except:
        print(" *ERROR: Interval must be >= 1!")
        return getIntervalOfTable()
    else:
        if (num < 1):
            print(" *ERROR: Interval must be >= 1!")
            return getIntervalOfTable()
        return num

# a function that displays the table
def displayTable(min, max, interval):
    print("n    Seq    Bin   Perf")
    print("--------------------------------")
    n = min
    while (n < max):
        print(f"{n}   {sequentialSearchComparisons(n)}   {binarySearchComparisons(n)}   {calculatePerformance(n)}")
        n += interval

    
# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def sequentialSearchComparisons(size):
    return math.floor(size / 2)

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the maximum number of comparisons
def binarySearchComparisons(size):
    return math.ceil(math.log(size + 1, 2))

# a function that calculates the performance of binary search compared to sequential search
# -input: the list size
# -output: the performance ratio
def calculatePerformance(size):
    return math.ceil((sequentialSearchComparisons(size) / binarySearchComparisons(size)) - 0.5)
    


###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
minVal = getMinOfTable()

# get user input for the maximum (make sure that is is >= minimum)
maxVal = getMaxOfTable(minVal)

# get user input for the interval (make sure that it is >= 1)
interval = getIntervalOfTable()

# generate the table
displayTable(minVal, maxVal, interval)

