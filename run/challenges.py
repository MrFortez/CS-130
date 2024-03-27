''' For testing challenges - DO NOT CHANGE THIS CODE '''
from audioop import avg


def check(chLet, func, answer, arg1, arg2 = None):
  if (arg2 is None):
    print(f"Challenge {chLet}: Testing {func.__name__} with {arg1} -> " + ('FAILED','PASSED')[func(arg1) == answer])
  else:
    print(f"Challenge {chLet}: Testing {func.__name__} with {arg1} and {arg2} -> " + ('FAILED','PASSED')[func(arg1, arg2) == answer])



############# Your code for ALL challenges goes here!  #################
#############       \/ Write Your Code Below \/        #################

''' Challenge A '''
# put challenge function here
def averageOfEven(list):
  sum = 0
  count = 0
  for x in list:
    if (x % 2 == 0):
      sum += x
      count += 1
  if (count == 0):
    return 0
  return sum / count

# test (uncomment to test challenge A)
# check('A', averageOfEven, 5.0, [3, 5, 8, 2, 1, 3, 7])
# check('A', averageOfEven, 8.8, [12, 8, 22, 2, 0])
# check('A', averageOfEven, 0.0, [7, 47, 3])
print()




''' Challenge B '''
# put challenge function here
def secondLargest(list):
  list.sort()
  return list[len(list) - 2]



# test (uncomment to test challenge B)
# check('B',secondLargest, 5, [3, 5, 8, 2, 1])
# check('B',secondLargest, 4, [1, 2, 3, 4, 5])
# check('B',secondLargest, 6, [8, 6, 4, 2, 1])
# check('B',secondLargest, 17, [17, 18, 11, 13, 12])
# check('B',secondLargest, 15, [ 9,  8,  7,  6,  3, 23, 15])
# check('B',secondLargest, 42, [42, 180])
# check('B',secondLargest, 42, [180, 42])
# print()




''' Challenge C '''
# put both challenge functions here
def isPrime(num): 
  if (num == 2 or num == 3 or num == 5):
    return True
  if (num % 2 == 0 or num == 0 or num == 1):
    return False
  i = 3
  while (i <= num / 2):
    if (num % i == 0):
      return False
    i += 2
  return True

def findFirstPrime(list):
  for x in list:
    if (isPrime(x)):
      return x
  return -1




# test (uncomment to test challenge C)
# check('C', findFirstPrime,  3, [3,  5,  8, 2, 1])
# check('C', findFirstPrime, 17, [1,  9, 17, 0])
# check('C', findFirstPrime, -1, [8, 15, 20])
# check('C', findFirstPrime,  2, [9, 15,  4, 2])
# check('C', isPrime, False, 0)
# check('C', isPrime, False, 1)
# check('C', isPrime, True,  2)
# check('C', isPrime, True,  3)
# check('C', isPrime, False, 4)
# check('C', isPrime, True,  5)
# check('C', isPrime, False, 9)
# print()




''' Challenge D '''
# put challenge function here
def getColors(list):
  inList = []
  colors = ["red", 'orange', 'yellow', 'blue']
  for item in list:
    for color in colors:
      if item.lower() == color:
        inList.append(item)
  return inList

# test (uncomment to test challenge D)
# check('D', getColors, ["blue", "orange"], ["blue", "keyboard", "not a color", "orange"])
# check('D', getColors, ["YeLloW", "Red", "rEd", "reD"], ["7", "YeLloW", "Red", "rEd", "reD", "xbluex"])
# check('D', getColors, [], ["no", "yes", "mouse", "python", " blue"])
# print()




''' Challenge E '''
# put challenge function here
def partitionChars(charList):
  numList = []
  letterStr = ""
  for char in charList:
    try:
      numList.append(int(char))
    except:
      letterStr += char
  return [(sum(numList)), letterStr]


# test (uncomment to test challenge E)
# check('E', partitionChars, [8, 'ja'], ['5', '3', 'j', 'a'])
# check('E', partitionChars, [10, 'abDE'], ['a', 'b', '4', 'D', '6', 'E'])
# check('E', partitionChars, [11, 'Rj'], ['0', '2', '7', '2', '0', 'R', 'j'])
# check('E', partitionChars, [0, 'abaa'], ['a', 'b', 'a', 'a'])
# check('E', partitionChars, [24, ''], ['8', '1', '4', '5', '2', '4'])
# check('E', partitionChars, [0, ''], [])
# print()




''' Challenge F '''
# put challenge function here

# this one is pretty hard, so I'll give you an outline of the logic:

# create function header
#     convert the number into a string
#     check if index is higher than the position of the last digit in the string
#     if it is
#         return 0
#     if it isn't
#         check if the digit at the index is a 9
#         if it is
#             return 1 plus the result of a recursive call to the function sending the number and index + 1 as arguments
#         if it isn't
#             return the result of a recursive call to the function sending the number and index + 1 as arguments
def countTheNines(num, i):
  numStr = str(num)
  if (i > len(numStr) - 1):
    return 0
  else:
    if (numStr[i] == "9"):
      return 1 + countTheNines(num, i + 1)
    else:
      return countTheNines(num, i + 1)



# test (uncomment to test challenge F)
check('F', countTheNines, 2, 29839, 0)
check('F', countTheNines, 0, 0, 0)
check('F', countTheNines, 1, 12748194, 0)
# print()




''' Challenge G '''
# put all 3 challenge functions here
def containsOneW(str):
  count = 0
  for char in str:
    if (char == "W"):
      count += 1
  return count == 1

def containsOneWandO(str):
  count = 0
  for char in str:
    if (char == "o"):
      count += 1
  return count == 1 and containsOneW(str)

def containsTheWordWon(str):
  nCheck = False
  for char in str:
    if (char == "n"):
      nCheck = True
  return nCheck and containsOneWandO(str)



# test (uncomment to test challenge G)
check('G', containsTheWordWon, False, 'You just Won!')
check('G', containsTheWordWon, True, 'Mousey is a Winner!')
check('G', containsTheWordWon, True, 'You are a Winner!')
check('G', containsTheWordWon, True, 'Team has Won!')
