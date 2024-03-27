#################################################################################
# name: Brandon Fortes 
# date: October 13, 2023    
# description: A program that takes 3 user-given numbers and then determines certain properties about the numbers
#################################################################################

# A function that prompts the user for a number and returns it.
def getUserNum():
    try:
        num = int(input("Enter a number:   "))
    except:
        print("thats not an integer silly")
        return getUserNum()
    else:
        return num

# A function that receives any amount of numbers as arguments, and returns the
# largest of the numbers.
def getMax(*nums):
    max = nums[0]
    i = 0
    while (i < len(nums)):
        if (nums[i] > max):
            max = nums[i]
        i += 1
    return max

# A function that receives three numbers as arguments, and returns the
# product of the two largest arguments.
def getHighestProduct(numA, numB, numC):
    if ((numA * numB) > (numA * numC) and (numA * numB) > (numB * numC)):
        return numA * numB
    elif ((numA * numC) > (numB * numC)):
        return numA * numC
    else:
        return numB * numC

# A function that receives an argument and returns a string representing
# whether that argument is even or odd.
def isEven(num):
    if (num % 2 == 0):
        return "even"
    return "odd"

# A function that receives an argument and determines whether that
# argument is a prime number.
def isPrime(num):
    if (num == 2 or num == 3 or num == 5 or num == 7):
        return True
    if (num % 2 == 0):
        return False
    i = 3
    while (i < (num / 2)):
        if (num % i == 0):
            return False
        i += 2
    return True



##################################### MAIN PROGRAM #######################
# Functions that were defined above should be executed below in an order
# that satisfies the original problem statement. Additional statements
# can be included if needed.
##########################################################################

# Prompt for three different numbers and store them appropriately.
numberA = getUserNum()
numberB = getUserNum()
numberC = getUserNum()

# Print "out the table header information.
print("--------------------")
print("Num  Even  Prime")
print("--------------------")

# Print out the table contents for each of the three numbers.
print(F"{numberA}  {isEven(numberA)}   {isPrime(numberA)}")
print(F"{numberB}  {isEven(numberB)}   {isPrime(numberB)}")
print(F"{numberC}  {isEven(numberC)}   {isPrime(numberC)}")

# Print out the" identity of the largest number and the largest product
# from the given numbers.
print("--------------------")
print(f"The largest number is {getMax(numberA, numberB, numberC)}")
print(f"The largest possible product is {getHighestProduct(numberA, numberB, numberC)}")