''' Challenge A '''
# put challenge function here
def listAverage(list):
    if (len(list) == 0):
        return -1
    return sum(list) / len(list)



# test (uncomment to test challenge A)
print(listAverage([1,2,3,4,5,6]) == 3.5)
print(listAverage([4,5,7,8,3]) == 5.4)
print(listAverage([8]) == 8)
print(listAverage([]) == -1)



''' Challenge B '''
# put challenge function here
def strToList(str):
    str = list(str)
    return str


# test (uncomment to test challenge B)
print(strToList("hello world") == ['h','e','l','l','o',' ','w','o','r','l','d'])
print(strToList("123456") == ['1','2','3','4','5','6'])
print(strToList("5Hello78!!") == ['5','H','e','l','l','o','7','8','!','!'])
print(strToList("") == [])



''' Challenge C '''
# put challenge function here
def findNumbers(str):
    list = []
    for char in str:
        try: 
            int(char)
        except:
            pass
        else:
            list.append(int(char))
    return list




# test (uncomment to test challenge C)
print(findNumbers("p7y679th0n") == [7, 6, 7, 9, 0])
print(findNumbers("python") == [])
print(findNumbers("") == [])

