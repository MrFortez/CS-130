##############################################################################
# author: Brandon Fortes    
# date: November 3, 2023
# description:
#############################################################################

# A function that prompts the user for the number of people this program
# will be comparing.
def getPeopleCount():
    return int(input("How many people are you comparing? "))

# A function that receives the size of a list, and repeatedly prompts the user
# for that number of names. It then returns the complete list of names.
def createNameList(size):
    nameList = []
    i = 0
    while (i < size):
        nameList.append(input(f"What is the name of person number {i + 1}: "))
        i += 1
    return nameList

# A function that receives the size of a list, and repeatedly prompts
# the user for that number of ages. It then returns the complete list of
# ages.
def createAgeList(size):
    ageList = []
    i = 0
    while (i < size):
        ageList.append(int(input(f"What is the age of person number {i + 1}: ")))
        i += 1
    return ageList

# A function that recieves a list and searches it. It then returns the index
# of the smallest value in the list
def findListMin(list):
    minIndex = 0
    for i in range(0, len(list)):
        if (list[minIndex] > list[i]):
            minIndex = i
    return minIndex

# A function that recieves a list and searches it. It then returns the index
# of the largest value in the list
def findListMax(list):
    maxIndex = 0
    for i in range(0, len(list)):
        if (list[maxIndex] < list[i]):
            maxIndex = i
    return maxIndex

# A function that recieves a list and finds the average of all of the values in the list.
# It then returns the average
def getListAverage(list):
    sum = 0
    for x in list:
        sum += x
    return sum / len(list)

################################ MAIN ################################
# Ask for the number of people using one of the functions defined above.
size = getPeopleCount()
print("----------------------------------------")

# Ask for the names of the people using one of the functions defined
# above.
nameList = createNameList(size)
print("----------------------------------------")

# Ask for the ages of the people using one of the functions defined
# above.
ageList = createAgeList(size)
print("----------------------------------------")

# Identify the names of the youngest and oldest people in the list.
minAgeIndex = findListMin(ageList)
maxAgeIndex = findListMax(ageList)
print(f"{nameList[minAgeIndex]} is the youngest at {ageList[minAgeIndex]} years old")
print(f"{nameList[maxAgeIndex]} is the oldest at {ageList[maxAgeIndex]} years old")

# Display information about the lists.
print(f"The average age is {getListAverage(ageList)}")
