

# def div3(num): 
#     return (num % 3 == 0)

# i = 1
# while (i <= 10):
#     if (div3(i)):
#         print(i)
#     i += 1


# i = 1
# j = 1
# while (i <= 10):
#     j = 0
#     while (j <= 10):
#         print(f"{i}*{j} = " + str(i * j))
#         j += 1
#     i += 1

def isEven(num):
    if (num % 2 == 0):
        return "Even"
    else:
        return "Not Even"


print(isEven(int(input("Enter a number: "))))

